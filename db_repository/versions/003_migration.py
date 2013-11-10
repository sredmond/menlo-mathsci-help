from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
post = Table('post', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('body', String),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
)

request = Table('request', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('class_for', String(length=64)),
    Column('issue', String(length=64)),
    Column('body', String(length=255)),
    Column('extra_requests', String(length=255)),
    Column('availability', String(length=255)),
    Column('additional', String(length=255)),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
)

user = Table('user', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String),
    Column('email', String),
    Column('role', SmallInteger),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('email', String(length=120)),
    Column('hashed_password', String(length=60)),
    Column('first_name', String(length=20)),
    Column('last_name', String(length=20)),
    Column('grade', SmallInteger),
    Column('role', SmallInteger, default=ColumnDefault(0)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].drop()
    post_meta.tables['request'].create()
    pre_meta.tables['user'].columns['nickname'].drop()
    post_meta.tables['user'].columns['first_name'].create()
    post_meta.tables['user'].columns['grade'].create()
    post_meta.tables['user'].columns['hashed_password'].create()
    post_meta.tables['user'].columns['last_name'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].create()
    post_meta.tables['request'].drop()
    pre_meta.tables['user'].columns['nickname'].create()
    post_meta.tables['user'].columns['first_name'].drop()
    post_meta.tables['user'].columns['grade'].drop()
    post_meta.tables['user'].columns['hashed_password'].drop()
    post_meta.tables['user'].columns['last_name'].drop()
