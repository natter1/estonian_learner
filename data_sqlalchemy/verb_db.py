"""
@author: Nathanael Jöhrmann
@license: MIT
"""

import datetime
import textwrap

import sqlalchemy as sa

from data_sqlalchemy.conjugations_db import ConjugationsDB
from data_sqlalchemy.modelbase import SqlAlchemyBase


class VerbDB(SqlAlchemyBase):
    """
    Class vor a verb (estonian). For use with SQLAlchemy.
    """
    __tablename__ = "verbs"
    # id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    hint = sa.Column(sa.String)  # not supported by sqlite: nullable=True

    infinitive_ma = sa.Column(sa.String, primary_key=True)  # , index=True)
    infinitive_da = sa.Column(sa.String)
    past_active_participle = sa.Column(sa.String)
    past_passive_participle = sa.Column(sa.String)

    infinitive_ma_english = sa.Column(sa.String)
    infinitive_da_english = sa.Column(sa.String)
    past_active_participle_english = sa.Column(sa.String)
    past_passive_participle_english = sa.Column(sa.String)

    # Conjugations
    present = sa.Column(sa.JSON)
    conditional_mood = sa.Column(sa.JSON)
    imperative_mood = sa.Column(sa.JSON)
    imperative_negative_mood = sa.Column(sa.JSON)

    perfect = sa.Column(sa.JSON)
    past = sa.Column(sa.JSON)
    plusperfect = sa.Column(sa.JSON)
    conditional_perfect_mood = sa.Column(sa.JSON)

    quotative = sa.Column(sa.JSON)
    quotative_perfect = sa.Column(sa.JSON)
    jussive = sa.Column(sa.JSON)
    jussive_perfect = sa.Column(sa.JSON)

    # dict
    other = sa.Column(sa.JSON)

    usage_info = sa.Column(sa.String)

    audio = sa.Column(sa.BLOB)

    def __init__(self):
        self.usage_info = ""
        self.audio = None

    def __repr__(self) -> str:  # for more useful debug messages
        return f"<VerbDB {self.infinitive_ma}>"

    @property
    def summary(self) -> str:
        """
        Returns a summary with all conjugations for all tenses, moods ... .

        :return: A summary of all conjugations.
        """
        def get_conjugations_summary(json_dict: dict) -> str:
            conjugations = ConjugationsDB()
            conjugations.from_json(json_dict)
            return conjugations.summary

        result = textwrap.dedent(f"""\
            ---------------------------------------------------------
            Usage info:
            {self.usage_info}\n
            Infinitive (-ma  -da  translation):
            {self.infinitive_ma}  {self.infinitive_da}  {self.infinitive_ma_english}\n
            Past active participle:
            {self.past_active_participle}  {self.past_active_participle_english}\n
            Past passive participle:
            {self.past_passive_participle}  {self.past_passive_participle_english}\n
            Present tense:
            """)

        result += get_conjugations_summary(self.present)

        result += "\nConditional mood\n"
        result += get_conjugations_summary(self.conditional_mood)

        result += "\nImperative mood\n"
        result += get_conjugations_summary(self.imperative_mood)

        result += "\nImperative negative mood\n"
        result += get_conjugations_summary(self.imperative_negative_mood)

        result += "\nPerfect tense\n"
        result += get_conjugations_summary(self.perfect)

        result += "\nPast tense\n"
        result += get_conjugations_summary(self.past)

        result += "\nPlusperfect tense\n"
        result += get_conjugations_summary(self.plusperfect)

        result += "\nConditional perfect mood\n"
        result += get_conjugations_summary(self.conditional_perfect_mood)

        result += "\nQuotative tense\n"
        result += get_conjugations_summary(self.quotative)

        result += "\nQuotative perfect tense\n"
        result += get_conjugations_summary(self.quotative_perfect)

        result += "\nJussive tense\n"
        result += get_conjugations_summary(self.jussive)

        result += "\nJussive perfect tense\n"
        result += get_conjugations_summary(self.jussive_perfect)

        result += "\nOther\n"
        for key in self.other:
            result += key + "  " + self.other[key][0] + "  " + self.other[key][1] + "\n"

        result += "---------------------------------------------------------\n"
        return result
