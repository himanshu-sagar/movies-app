"""empty message

Revision ID: 7ac9bee5cd61
Revises: 7b5c3a22b7dd
Create Date: 2022-12-31 09:07:06.028396

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ac9bee5cd61'
down_revision = '7b5c3a22b7dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.alter_column('poster_path',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=250),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.alter_column('poster_path',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###
