"""
@author: Nathanael Jöhrmann
@license: MIT
"""

import datetime
import json

from data_sqlalchemy.modelbase import SqlAlchemyBase
import sqlalchemy as sa

# not used in DB; Conjugation is stored as JSON dict in VerbDB
class ConjugationsDB:  # (SqlAlchemyBase):
    """
    Class containing conjugations for first to sixted person, negative, passive and passive negative.
    """
    __tablename__ = "conjugations"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    hint = sa.Column(sa.String)  # not supported by sqlite: nullable=True
    tense = sa.Column(sa.String)  # todo: check ENUM
    data_json = sa.Column(sa.JSON)

    @property
    def summary(self) -> str:
        """
        Returns a summary with all conjugations.

        :return: A summary of all conjugations.
        """
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
        Returns a jsonified dict containing the data from self.data_json.

        :return: dict
        """
        my_dict = self.data_json
        result = json.loads(json.dumps(my_dict, indent=2, ensure_ascii=False))
        # print((my_dict))
        # print(result)
        # todo: check, weather copy is needed
        # return my_dict  # todo: test if this works with SQLAlchemy
        return result

    def from_json(self, _json: dict) -> None:
        """
        This reads ConjugationsDB.data_json from a jsonified dict _json.

        :param _json: A jsonified dict
        :type _json: dict
        :return: None
        """
        self.data_json = _json
