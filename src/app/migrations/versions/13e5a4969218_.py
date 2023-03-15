"""empty message

Revision ID: 13e5a4969218
Revises: 
Create Date: 2023-03-14 14:52:20.487637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13e5a4969218'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('h_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_data', sa.String(length=16000), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('h_data')
    # ### end Alembic commands ###
