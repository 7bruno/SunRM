"""empty message

Revision ID: 5418dabfc62e
Revises: 
Create Date: 2021-01-11 20:59:04.572048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5418dabfc62e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hsp',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=80), nullable=False),
    sa.Column('uf', sa.String(length=120), nullable=False),
    sa.Column('md_anual', sa.Integer(), nullable=False),
    sa.Column('lon', sa.Numeric(), nullable=False),
    sa.Column('lat', sa.Numeric(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('city'),
    sa.UniqueConstraint('uf')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hsp')
    # ### end Alembic commands ###