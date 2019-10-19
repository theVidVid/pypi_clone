import sqlalchemy as sa
from pypi_org.data.modelbase import SqlAlchemyBase


class Maintainer(SqlAlchemyBase):
    """A class representing a maintainer of a particular package."""
    __tablename__ = 'maintainers'
    __table_args__ = {'extend_existing': True}

    user_id = sa.Column(sa.Integer, primary_key=True)
    package_id = sa.Column(sa.String, primary_key=True)
