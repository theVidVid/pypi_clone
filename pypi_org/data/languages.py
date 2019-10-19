import datetime
import sqlalchemy
from pypi_org.data.modelbase import SqlAlchemyBase


class ProgrammingLanguage(SqlAlchemyBase):
    """A class representing a particular programming language."""
    __tablename__ = 'languages'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now, index=True)
    description = sqlalchemy.Column(sqlalchemy.String)
