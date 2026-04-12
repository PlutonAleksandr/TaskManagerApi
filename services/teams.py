from database import session_factory
from models.teams import Teams
from schemas.team import TeamCreateSchema, TeamResponseSchema, TeamUpdate


class TeamsCRUD:

    @staticmethod
    def create_team(team_data:TeamCreateSchema) -> Teams:
        with session_factory() as session:
            team = Teams(team_name=team_data.team_name)
            session.add(team)
            session.commit()
            session.refresh(team)
            return team

    @staticmethod
    def select_team(id: int) -> Teams | None:
        with session_factory() as session:
            return session.get(Teams, id)

    @staticmethod
    def select_all_teams() -> list[Teams]:
        with session_factory() as session:
            return session.query(Teams).all()

    @staticmethod
    def update_team(id: int, new_data: TeamUpdate) -> Teams | None:
        with session_factory() as session:
            team = session.get(Teams, id)
            if not team:
                return None

            if new_data.team_name is not None:
                team.team_name = new_data.team_name

            session.commit()
            session.refresh(team)
            return team

    @staticmethod
    def delete_team(team_id: int) -> bool:
        with session_factory() as session:
            team = session.get(Teams, team_id)
            if not team:
                return False

            session.delete(team)
            session.commit()
            return True
