"""
This module helps to read estonian sentences into the corresponding objects.
A fitting source has to be included into ..\\resources\\estonian_sentences.txt

@author: Nathanael Jöhrmann
@license: MIT
"""

import os
import csv

from data_sqlalchemy import estonian_database
from data_sqlalchemy.db_session import DbSession
from data_sqlalchemy.sentence_db import SentenceDB


db_file = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "db",
        "estonian.sqlite"
    ))


def main():
    my_sentences = read_sentence_source_file()
    print(my_sentences)

    add_to_database(my_sentences)


def read_sentence_source_file() -> list:
    result = []
    sentences_source = "..\\resources\\estonian_sentences.txt"  # file containing estonian sentences
    with open(sentences_source, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')

        for row in csv_reader:
            if len(row) < 2:
                continue
            my_sentence = SentenceDB()
            my_sentence.estonian = row[0]
            my_sentence.english = row[1]
            result.append(my_sentence)

    return result


def get_sentences_from_database() -> list:
    estonian_database.create(db_file)

    session = DbSession.factory()
    result = session.query(SentenceDB).all()
    session.commit()

    return result


def get_sentence_from_database(estonian: str):
    estonian_database.create(db_file)

    session = DbSession.factory()
    result = session.query(SentenceDB).get({"estonian": estonian})

    return result


def add_to_database(my_sentences):

    estonian_database.create(db_file)

    session = DbSession.factory()
    for sentence in my_sentences:
        session.merge(sentence)

    session.commit()




if __name__ == "__main__":
    main()
