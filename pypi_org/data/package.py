import datetime
import sqlalchemy as sa
import sqlalchemy.orm as orm

from data.releases import Release
from pypi_org.data.modelbase import SqlAlchemyBase


class Package(SqlAlchemyBase):
    """Class representing Packages from Pypi.org"""

    # Database table name will be packages instead of class name 'Package'
    __tablename__ = 'packages'

    id = sa.Column(sa.String, primary_key=True)
    created_date = sa.Column(sa.DATETIME, default=datetime.datetime.now,
                             index=True)
    summary = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String, nullable=True)

    home_page = sa.Column(sa.String)
    docs_url = sa.Column(sa.String)
    package_url = sa.Column(sa.String)

    author_name = sa.Column(sa.String)
    author_email = sa.Column(sa.String, index=True)

    license = sa.Column(sa.String, index=True)

    # DB relationship of releases
    releases = orm.relation("Release", order_by=[
        Release.major_ver.desc(),
        Release.minor_ver.desc(),
        Release.build_ver.desc(),
    ], back_populates='package')

    # maintainers

    def __repr__(self):
        return f'<Package {self.id}>'
