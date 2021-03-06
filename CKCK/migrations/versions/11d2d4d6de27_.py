"""empty message

Revision ID: 11d2d4d6de27
Revises: 96b3f37544be
Create Date: 2020-08-20 11:09:08.242131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11d2d4d6de27'
down_revision = '96b3f37544be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usercontent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('filename', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['username'], ['user.username'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usercontent')
    # ### end Alembic commands ###
