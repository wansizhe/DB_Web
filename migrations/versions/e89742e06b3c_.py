"""empty message

Revision ID: e89742e06b3c
Revises: fa91070a5149
Create Date: 2018-01-15 16:31:07.627212

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e89742e06b3c'
down_revision = 'fa91070a5149'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('reports_ibfk_4', 'reports', type_='foreignkey')
    op.drop_column('reports', 'admin_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reports', sa.Column('admin_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('reports_ibfk_4', 'reports', 'users', ['admin_id'], ['id'])
    # ### end Alembic commands ###
