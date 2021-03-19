"""empty message

Revision ID: 2ed30baac322
Revises: 
Create Date: 2021-03-19 14:30:46.793746

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ed30baac322'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('propertyDesc', sa.String(length=160), nullable=True),
    sa.Column('NoOfBedrooms', sa.String(length=10), nullable=True),
    sa.Column('NoOfBathrooms', sa.String(length=10), nullable=True),
    sa.Column('price', sa.String(length=20), nullable=True),
    sa.Column('propertyType', sa.String(length=20), nullable=True),
    sa.Column('location', sa.String(length=80), nullable=True),
    sa.Column('photo', sa.String(length=160), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    # ### end Alembic commands ###