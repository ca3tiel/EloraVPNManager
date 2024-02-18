"""Add Notification models

Revision ID: 8c6b724752e9
Revises: d8b2d9e1700d
Create Date: 2023-10-04 00:49:59.906398

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8c6b724752e9"
down_revision = "d8b2d9e1700d"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "notification",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("account_id", sa.Integer(), nullable=True),
        sa.Column("level", sa.Integer(), nullable=True),
        sa.Column("message", sa.String(length=4096), nullable=True),
        sa.Column("details", sa.String(length=10000), nullable=True),
        sa.Column("approve", sa.Boolean(), nullable=True),
        sa.Column(
            "engine",
            sa.Enum("telegram", "email", "sms", name="notificationengine"),
            nullable=False,
        ),
        sa.Column(
            "status",
            sa.Enum("pending", "canceled", "failed", "sent", name="notificationstatus"),
            nullable=False,
        ),
        sa.Column(
            "type",
            sa.Enum("used_traffic", "expire_time", name="notificationtype"),
            nullable=False,
        ),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("modified_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["account_id"],
            ["account.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_notification_id"), "notification", ["id"], unique=False)
    op.create_index(
        op.f("ix_notification_level"), "notification", ["level"], unique=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_notification_level"), table_name="notification")
    op.drop_index(op.f("ix_notification_id"), table_name="notification")
    op.drop_table("notification")
    # ### end Alembic commands ###
