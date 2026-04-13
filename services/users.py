from database import session_factory
from models import Teams, Users
from schemas.user import UserCreate, UserUpdate


class UsersCRUD:
    @staticmethod
    def _validate_team(session, team_id: int | None):
        if team_id is None:
            return

        if not session.get(Teams, team_id):
            raise ValueError("Команда не найдена")

    @staticmethod
    def create_user(user_data: UserCreate) -> Users:
        with session_factory() as session:

            UsersCRUD._validate_team(session, user_data.team_id)

            user = Users(
                username=user_data.username,
                age=user_data.age,
                team_id=user_data.team_id
            )
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    @staticmethod
    def select_user(id: int) -> Users | None:
        with session_factory() as session:
            return session.get(Users, id)

    @staticmethod
    def select_all_users() -> list[Users]:
        with session_factory() as session:
            return session.query(Users).all()

    @staticmethod
    def update_user(id: int, new_data: UserUpdate) -> Users | None:
        with session_factory() as session:
            user = session.get(Users, id)
            if not user:
                return None

            update_dict = new_data.model_dump(exclude_unset=True)

            if "team_id" in update_dict:
                UsersCRUD._validate_team(session, update_dict["team_id"])

            for field, value in update_dict.items():
                setattr(user, field, value)

            session.commit()
            session.refresh(user)
            return user

    @staticmethod
    def delete_user(id: int) -> bool:
        with session_factory() as session:
            user = session.get(Users, id)
            if not user:
                return False

            session.delete(user)
            session.commit()
            return True