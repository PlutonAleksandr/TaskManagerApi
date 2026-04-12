from sqlalchemy import select

from database import session_factory
from models.statuses import TaskStatus
from models import Teams, Users, Tasks
from schemas.task import TaskCreateSchema, TaskUpdateSchema


class TasksCRUD:

    @staticmethod
    def _validate_assignment(session, user_id: int | None, team_id: int | None) -> None:
        if user_id is not None:
            user = session.get(Users, user_id)
            if not user:
                raise ValueError("Пользователь не найден")

        if team_id is not None:
            team = session.get(Teams, team_id)
            if not team:
                raise ValueError("Команда не найдена")

    @staticmethod
    def create_task(task_data: TaskCreateSchema) -> Tasks:
        with session_factory() as session:
            TasksCRUD._validate_assignment(session, task_data.user_id, task_data.team_id)

            task = Tasks(
                title=task_data.title,
                priority=task_data.priority,
                description=task_data.description,
                deadline=task_data.deadline,
                status=task_data.status,
                user_id=task_data.user_id,
                team_id=task_data.team_id
            )

            session.add(task)
            session.commit()
            session.refresh(task)

            return task

    @staticmethod
    def select_task_by_id(id: int) -> Tasks | None:
        with session_factory() as session:
            return session.get(Tasks, id)

    @staticmethod
    def select_task_by_status(status: TaskStatus) -> list[Tasks]:
        with session_factory() as session:
            query = select(Tasks).where(Tasks.status == status)
            result = session.execute(query)
            return result.scalars().all()

    @staticmethod
    def select_tasks_by_id(list_id: list[int]) -> list[Tasks]:
        with session_factory() as session:
            query = select(Tasks).where(Tasks.id.in_(list_id))
            return session.execute(query).scalars().all()

    @staticmethod
    def update_task(task_id: int, update_data: TaskUpdateSchema) -> Tasks | None:
        with session_factory() as session:
            task = session.get(Tasks, task_id)

            if not task:
                return None

            new_user_id = update_data.user_id if update_data.user_id is not None else task.user_id
            new_team_id = update_data.team_id if update_data.team_id is not None else task.team_id

            if new_user_id is not None and new_team_id is not None:
                raise ValueError("Задача не может быть назначена и пользователю и команде одновременно")

            TasksCRUD._validate_assignment(session, update_data.user_id, update_data.team_id)

            update_dict = update_data.model_dump(exclude_unset=True)

            for field, value in update_dict.items():
                setattr(task, field, value)

            session.commit()

            return task

    @staticmethod
    def update_tasks_by_status(list_id: list[int], new_status: TaskStatus) -> None:
        with session_factory() as session:
            query = select(Tasks).where(Tasks.id.in_(list_id))
            tasks = session.execute(query).scalars().all()

            for task in tasks:
                task.status = new_status

            session.commit()

    @staticmethod
    def delete_task(task_id: int) -> bool:
        with session_factory() as session:
            task = session.get(Tasks, task_id)
            if not task:
                return False

            session.delete(task)
            session.commit()

            return True