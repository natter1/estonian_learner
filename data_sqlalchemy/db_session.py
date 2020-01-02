import sqlalchemy as sa
import sqlalchemy.orm as orm

from data_sqlalchemy.modelbase import SqlAlchemyBase


class DbSession:
    factory = None
    engine = None

    @classmethod
    def global_init(cls, db_file: str):
        if cls.factory:
            return

        if not db_file or not db_file.strip():
            raise Exception("You must specify a db file")

        connection_str = "sqlite:///" + db_file.strip()
        print(f"Connecting to DB with {connection_str}")

        cls.engine = sa.create_engine(connection_str, echo=False)
        cls.factory = orm.sessionmaker(bind=cls.engine)

        # noinspection PyUnresolvedReferences
        import data_sqlalchemy.__all_models

        SqlAlchemyBase.metadata.create_all(DbSession.engine)



