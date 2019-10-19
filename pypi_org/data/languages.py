import datetime
import sqlalchemy as sa
from pypi_org.data.modelbase import SqlAlchemyBase


class ProgrammingLanguage(SqlAlchemyBase):
    """A class representing a particular programming language."""
    __tablename__ = 'languages'
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.String, primary_key=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now,
                             index=True)
    description = sa.Column(sa.String)
