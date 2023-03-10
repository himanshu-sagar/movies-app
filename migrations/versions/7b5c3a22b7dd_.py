"""empty message

Revision ID: 7b5c3a22b7dd
Revises: 405b33977e5d
Create Date: 2022-12-31 09:02:15.155631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b5c3a22b7dd'
down_revision = '405b33977e5d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.alter_column('overview',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=500),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.alter_column('overview',
               existing_type=sa.String(length=500),
               type_=sa.VARCHAR(length=100),
               existing_nullable=True)

    # ### end Alembic commands ###
