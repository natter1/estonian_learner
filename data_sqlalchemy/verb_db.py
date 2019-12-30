import datetime

from data_sqlalchemy.modelbase import SqlAlchemyBase
import sqlalchemy as sa


# not used; Conjugation is stored as JSON in VerbDB
from estonian_learner.verb import Conjugations


class ConjugationDB(SqlAlchemyBase):
    __tablename__ = "conjugations"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    hint = sa.Column(sa.String)  # not supported by sqlite: nullable=True
    tense = sa.Column(sa.String)  # todo: check ENUM
    data_json = sa.Column(sa.JSON)


class VerbDB(SqlAlchemyBase):
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
        # self.infinitive_ma = ("", "")
        # self.infinitive_da = ("", "")
        # self.past_active_participle = ("", "")
        # self.past_passive_participle = ("", "")
        #
        # self.present = Conjugations()
        # self.conditional_mood = Conjugations()
        # self.imperative_mood = Conjugations()
        # self.imperative_negative_mood = Conjugations()
        #
        # self.perfect = Conjugations()
        # self.past = Conjugations()
        # self.plusperfect = Conjugations()
        # self.conditional_perfect_mood = Conjugations()
        #
        # self.quotative = Conjugations()
        # self.quotative_perfect = Conjugations()
        # self.jussive = Conjugations()
        # self.jussive_perfect = Conjugations()
        #
        # self.other = {}

        self.usage_info = ""

        self.audio = None

    def __repr__(self):  # for more useful debug messages
        return f"<VerbDB {self.id}>"

    def get_summary(self):
        result = "\n---------------------------------------------------------"

        result += "\nUsage info:\n"
        result += self.usage_info + "\n"

        result += "\nInfinitive (-ma  -da  translation)\n"
        result += self.infinitive_ma + "  " + self.infinitive_da + "  " + self.infinitive_ma_english + "\n"

        result += "\nPast active participle\n"
        result += self.past_active_participle + "  " + self.past_active_participle_english + "\n"

        result += "\nPast passive participle\n"
        result += self.past_passive_participle + "  " + self.past_passive_participle_english + "\n"

        result += "\nPresent tense\n"
        conjugations = Conjugations()
        conjugations.from_json(self.present)
        result += conjugations.summary

        result += "\nConditional mood\n"
        conjugations = Conjugations()
        conjugations.from_json(self.conditional_mood)
        result += conjugations.summary

        result += "\nImperative mood\n"
        conjugations = Conjugations()
        conjugations.from_json(self.imperative_mood)
        result += conjugations.summary

        result += "\nImperative negative mood\n"
        conjugations = Conjugations()
        conjugations.from_json(self.imperative_negative_mood)
        result += conjugations.summary

        result += "\nPerfect tense\n"
        conjugations = Conjugations()
        conjugations.from_json(self.perfect)
        result += conjugations.summary

        result += "\nPast tense\n"
        conjugations = Conjugations()
        conjugations.from_json(self.past)
        result += conjugations.summary

        result += "\nPlusperfect tense\n"
        conjugations = Conjugations()
        conjugations.from_json(self.plusperfect)
        result += conjugations.summary

        result += "\nConditional perfect mood\n"
        conjugations = Conjugations()
        conjugations.from_json(self.conditional_perfect_mood)
        result += conjugations.summary

        result += "\nQuotative tense\n"
        conjugations = Conjugations()
        conjugations.from_json(self.quotative)
        result += conjugations.summary

        result += "\nQuotative perfect tense\n"
        conjugations = Conjugations()
        conjugations.from_json(self.quotative_perfect)
        result += conjugations.summary

        result += "\nJussive tense\n"
        conjugations = Conjugations()
        conjugations.from_json(self.jussive)
        result += conjugations.summary

        result += "\nJussive perfect tense\n"
        conjugations = Conjugations()
        conjugations.from_json(self.jussive_perfect)
        result += conjugations.summary

        #
        # result += "\nOther\n"
        # for key in self.other:
        #     result += key + "  " + self.other[key][0] + "  " + self.other[key][1] + "\n"

        result += "---------------------------------------------------------\n"
        return result
