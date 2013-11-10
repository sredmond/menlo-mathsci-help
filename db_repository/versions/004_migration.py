from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
learnersForSubjects = Table('learnersForSubjects', post_meta,
    Column('learner_id', Integer),
    Column('subject_id', Integer),
)

subject = Table('subject', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=100)),
)

tutorsForSubjects = Table('tutorsForSubjects', post_meta,
    Column('tutor_id', Integer),
    Column('subject_id', Integer),
)

request = Table('request', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('class_for', String),
    Column('issue', String),
    Column('body', String),
    Column('extra_requests', String),
    Column('availability', String),
    Column('additional', String),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
)

request = Table('request', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('issue', String(length=64)),
    Column('body', String(length=1023)),
    Column('extra_requests', String(length=255)),
    Column('availability', String(length=255)),
    Column('additional', String(length=255)),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
    Column('subject_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['learnersForSubjects'].create()
    post_meta.tables['subject'].create()
    post_meta.tables['tutorsForSubjects'].create()
    pre_meta.tables['request'].columns['class_for'].drop()
    post_meta.tables['request'].columns['subject_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['learnersForSubjects'].drop()
    post_meta.tables['subject'].drop()
    post_meta.tables['tutorsForSubjects'].drop()
    pre_meta.tables['request'].columns['class_for'].create()
    post_meta.tables['request'].columns['subject_id'].drop()
