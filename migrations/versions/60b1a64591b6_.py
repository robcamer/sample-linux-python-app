"""empty message

Revision ID: 60b1a64591b6
Revises: 
Create Date: 2019-02-12 22:50:11.474760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60b1a64591b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('azure_document',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('url', sa.Text(), nullable=True),
    sa.Column('category', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_table('visitor',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(length=100), nullable=True),
    sa.Column('browser', sa.Text(), nullable=True),
    sa.Column('operating_system', sa.Text(), nullable=True),
    sa.Column('date_visited', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('pk')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('visitor')
    op.drop_table('azure_document')
    # ### end Alembic commands ###
