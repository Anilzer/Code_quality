"""empty message

Revision ID: 4913cb3f5a05
Revises: 5ee767807344
Create Date: 2021-10-04 16:48:11.680029

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4913cb3f5a05'
down_revision = '5ee767807344'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lifetime_coupon', sa.Column('comment', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('lifetime_coupon', 'comment')
    # ### end Alembic commands ###
