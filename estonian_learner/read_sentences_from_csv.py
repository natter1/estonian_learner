"""
This module helps to read estonian sentences into the corresponding objects.
A fitting source has to be included into ..\\resources\\estonian_sentences.txt

@author: Nathanael Jöhrmann
@license: MIT
"""

import os
import csv

from data_sqlalchemy import create_database
from data_sqlalchemy.db_session import DbSession
from data_sqlalchemy.sentence_db import SentenceDB


def read_to_sentence_db_list() -> list:
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
