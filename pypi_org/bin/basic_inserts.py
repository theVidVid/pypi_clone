import os
import pypi_org.data.db_session as db_session
from pypi_org.data.package import Package


def main():
    init_db()
    while True:
        insert_a_package()


def insert_a_package():
    p = Package()
    p.id = input('Package id / name: ').strip().lower()

    p.summary = input('Package summary: ').strip()
    p.author_name = input('Author: ').strip()
    p.license = input('License: ').strip()


def init_db():
    top_folder = os.path.dirname(__file__)
    rel_file = os.path.join('..', 'db', 'pypi.sqlite')
    db_file = os.path.abspath(os.path.join(top_folder, rel_file))
    db_session.global_init(db_file)


if __name__ == '__main__':
    main()
