from database import session_factory
from models.users import Users
from schemas.user import UserCreate, UserUpdate


class UsersCRUD:

    @staticmethod
    def create_user(user_data: UserCreate) -> Users:
        with session_factory() as session:
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

            user.username = new_data.username
            user.age = new_data.age
            user.team_id = new_data.team_id

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