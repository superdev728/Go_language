"""Add display keyword

Revision ID: b346dcd75c14
Revises: 7f9e28ceb511
Create Date: 2022-02-13 20:07:29.452401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b346dcd75c14'
down_revision = '7f9e28ceb511'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('short_link', sa.Column('display_shortpath', sa.String(length=200), nullable=True))
    op.create_index(op.f('ix_short_link_display_shortpath'), 'short_link', ['display_shortpath'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_short_link_display_shortpath'), table_name='short_link')
    op.drop_column('short_link', 'display_shortpath')
    # ### end Alembic commands ###
