"""Create Role model

Revision ID: 540bd16c442f
Revises: 
Create Date: 2023-11-07 14:15:55.009400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '540bd16c442f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Role', sa.Column('type', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Role', 'type')
    # ### end Alembic commands ###