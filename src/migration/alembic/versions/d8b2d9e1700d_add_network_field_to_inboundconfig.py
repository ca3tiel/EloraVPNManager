"""Add network field to InboundConfig

Revision ID: d8b2d9e1700d
Revises: 704bb66b328f
Create Date: 2023-08-14 22:47:41.595808

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'd8b2d9e1700d'
down_revision = '704bb66b328f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inbound_config', sa.Column('network',
                                              sa.Enum('ws', 'tcp', name='inboundnetwork'), nullable=False,
                                              server_default='ws'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('inbound_config', 'network')
    # ### end Alembic commands ###