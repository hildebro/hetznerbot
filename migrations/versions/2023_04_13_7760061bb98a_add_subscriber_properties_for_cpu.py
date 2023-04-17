"""add subscriber properties for cpu

Revision ID: 7760061bb98a
Revises: 661d993d5c07
Create Date: 2023-04-13 21:47:25.104697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7760061bb98a'
down_revision = '661d993d5c07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscriber', sa.Column('threads', sa.Integer(), nullable=False, server_default="8"))
    op.add_column('subscriber', sa.Column('release_date', sa.Integer(), nullable=False, server_default="2010"))
    op.add_column('subscriber', sa.Column('multi_rating', sa.Integer(), nullable=False, server_default="5000"))
    op.add_column('subscriber', sa.Column('single_rating', sa.Integer(), nullable=False, server_default="1000"))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('subscriber', 'single_core_rating')
    op.drop_column('subscriber', 'multi_core_rating')
    op.drop_column('subscriber', 'release_date')
    op.drop_column('subscriber', 'threads')
    # ### end Alembic commands ###
