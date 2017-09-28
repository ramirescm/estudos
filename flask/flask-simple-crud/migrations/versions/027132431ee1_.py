"""empty message

Revision ID: 027132431ee1
Revises: 15f1afa469cf
Create Date: 2017-09-28 07:40:09.820291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '027132431ee1'
down_revision = '15f1afa469cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('cover_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'cover_path')
    # ### end Alembic commands ###
