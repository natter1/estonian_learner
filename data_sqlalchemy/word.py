import datetime

from data_sqlalchemy.modelbase import SqlAlchemyBase
import sqlalchemy as sa


class Word(SqlAlchemyBase):
    __tablename__ = "words"
    # id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    id = sa.Column(sa.String, primary_key=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    hint = sa.String()  # not supported by sqlite: nullable=True

    def __repr__(self):  # for more useful debug messages
        return f"<Package {self.id}>"
