import datetime
import json
import textwrap

import sqlalchemy as sa

from data_sqlalchemy.modelbase import SqlAlchemyBase


# not used in DB; Conjugation is stored as JSON dict in VerbDB
class ConjugationsDB(SqlAlchemyBase):
    __tablename__ = "conjugations"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    hint = sa.Column(sa.String)  # not supported by sqlite: nullable=True
    tense = sa.Column(sa.String)  # todo: check ENUM
    data_json = sa.Column(sa.JSON)

    @property
    def summary(self) -> str:
        result = ""
        sep = "\t\t"

        for i in range(1, 7):
            result += f"{i}P{sep}{self.person[str(i)][0]}{sep}{self.person[str(i)][1]}\n"

        result += f"negative{sep}{self.negative[0]}{sep}{self.negative[1]}\n"
        result += f"passive{sep}{self.passive[0]}{sep}{self.passive[1]}\n"
        result += f"passive negative{sep}{self.passive_negative[0]}{sep}{self.passive_negative[1]}\n"

        return result

    @property
    def person(self) -> dict:
        return self.data_json['person']

    @property
    def negative(self) -> dict:
        return self.data_json['negative']

    @property
    def passive(self) -> dict:
        return self.data_json['passive']

    @property
    def passive_negative(self) -> dict:
        return self.data_json['passive_negative']

    # def add_person(self, original, translation, index):
    #     self.person[index] = original
    #     self.person_translation[index] = translation

    def to_json(self) -> dict:
        """
        Returns a jsonified dict containing the data of self.
        :return: dict
        """
        my_dict = self.data_json
        result = json.loads(json.dumps(my_dict, indent=2, ensure_ascii=False))
        # print((my_dict))
        # print(result)
        # return my_dict  # todo: test if this works with SQLAlchemy
        return result

    def from_json(self, _json: dict) -> None:
        self.data_json = {}
        self.data_json = _json


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
        self.usage_info = ""
        self.audio = None

    def __repr__(self) -> str:  # for more useful debug messages
        return f"<VerbDB {self.infinitive_ma}>"

    @property
    def summary(self):
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
