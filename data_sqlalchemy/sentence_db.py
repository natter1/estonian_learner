"""
@author: Nathanael Jöhrmann
@license: MIT
"""

import datetime
import textwrap

import sqlalchemy as sa

from data_sqlalchemy.conjugations_db import ConjugationsDB
from data_sqlalchemy.modelbase import SqlAlchemyBase


class SentenceDB(SqlAlchemyBase):
    """
    Class vor a verb (estonian). For use with SQLAlchemy.
    """
    __tablename__ = "sentences"
    # id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    hint = sa.Column(sa.String)  # not supported by sqlite: nullable=True

    estonian = sa.Column(sa.String, primary_key=True)
    english = sa.Column(sa.String)

    level = sa.Column(sa.Integer)

    audio = sa.Column(sa.BLOB)

    def __init__(self):
        self.audio = None

    def __repr__(self) -> str:  # for more useful debug messages
        return f"<SentenceDB {self.estonian}>"

    @property
    def summary(self) -> str:
        """
        Returns a summary with estonian, english and level..
        """
        result = textwrap.dedent(f"""\
            ---------------------------------------------------------
            Estonian:
            {self.estonian}\n
            English:
            {self.english}\n
            Level:
            {self.level}\n
            ---------------------------------------------------------
            """)

        return result
