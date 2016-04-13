"""dateTimeRefactor

Revision ID: a87f915e4b62
Revises: cdcaa9c693e3
Create Date: 2016-04-10 12:59:01.396000

"""

# revision identifiers, used by Alembic.
revision = 'a87f915e4b62'
down_revision = 'cdcaa9c693e3'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_error_data():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_error_data():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def upgrade_job_tracker():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('submission', 'datetime_utc')
    op.add_column('submission', sa.Column('datetime_utc', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    ### end Alembic commands ###


def downgrade_job_tracker():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('submission', 'datetime_utc')
    op.add_column('submission', sa.Column('datetime_utc', sa.Text(), autoincrement=False, nullable=True))
    ### end Alembic commands ###


def upgrade_user_manager():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_user_manager():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###
