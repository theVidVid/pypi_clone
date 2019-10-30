import datetime
from typing import List
import sqlalchemy as sa
import sqlalchemy.orm as orm
from pypi_org.data.modelbase import SqlAlchemyBase
from pypi_org.data.releases import Release


class Package(SqlAlchemyBase):
    """Class representing Packages from Pypi.org"""

    # Database table name will be packages instead of class name 'Package'
    __tablename__ = 'packages'
    __table_args__ = {'extend_existing': True}

    id: str = sa.Column(sa.String, primary_key=True)
    created_date: datetime.datetime = sa.Column(sa.DATETIME,
                                                default=datetime.datetime.now,
                                                index=True)
    last_updated: datetime.datetime = sa.Column(sa.DATETIME,
                                                default=datetime.datetime.now,
                                                index=True)
    summary: str = sa.Column(sa.String, nullable=False)
    description: str = sa.Column(sa.String, nullable=True)

    home_page: str = sa.Column(sa.String)
    docs_url: str = sa.Column(sa.String)
    package_url: str = sa.Column(sa.String)

    author_name: str = sa.Column(sa.String)
    author_email: str = sa.Column(sa.String, index=True)

    license: str = sa.Column(sa.String, index=True)

    # DB relationship of releases
    releases: List[Release] = orm.relation("Release", order_by=[
        Release.major_ver.desc(),
        Release.minor_ver.desc(),
        Release.build_ver.desc(),
    ], back_populates='package')

    # maintainers

    def __repr__(self):
        return f'<Package {self.id}>'
