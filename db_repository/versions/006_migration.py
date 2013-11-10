from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('email', String(length=120)),
    Column('hashed_password', String(length=60)),
    Column('first_name', String(length=20)),
    Column('last_name', String(length=20)),
    Column('grade', SmallInteger),
    Column('created', DateTime),
    Column('last_logged_in', DateTime),
    Column('role', SmallInteger, default=ColumnDefault(0)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['created'].create()
    post_meta.tables['user'].columns['last_logged_in'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['created'].drop()
    post_meta.tables['user'].columns['last_logged_in'].drop()
