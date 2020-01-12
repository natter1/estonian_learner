from data_sqlalchemy.db_session import DbSession


def create(filename: str):
    DbSession.global_init(filename)
