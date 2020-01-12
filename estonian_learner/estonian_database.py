"""

"""
import os
import csv
from data_sqlalchemy.db_session import DbSession
from data_sqlalchemy.sentence_db import SentenceDB
from estonian_learner.read_sentences_from_csv import read_to_sentence_db_list

def main():
    estonian_db = EstonianDB("estonian.sqlite")

    # ... get sentences and verbs etc.
    my_data = []
    # sentences:
    my_data.extend(read_to_sentence_db_list())

    estonian_db.add_to_database(my_data)

    print(estonian_db.get_sentences_from_database())


class EstonianDB:
    def __init__(self, filename: str):
        self.path = self.get_default_path(filename)
        DbSession.global_init(self.path)

    def get_default_path(self, filename) -> str:
        return os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "db",
                filename
            ))

    def add_to_database(self, my_data: list) -> None:
        session = DbSession.factory()
        for data in my_data:
            session.merge(data)
        session.commit()
        # use only, when all my_verbs entries do not exist in database (Unique Constraint!)
        # session.add_all(my_verbs)

    def get_sentences_from_database(self) -> list:
        session = DbSession.factory()
        return session.query(SentenceDB).all()

    def get_sentence_from_database(self, estonian: str) -> DbSession:
        session = DbSession.factory()
        return session.query(SentenceDB).get({"estonian": estonian})


def add_verbs():
    pass


if __name__ == '__main__':
    main()
