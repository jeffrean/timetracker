"""timestamps table

Revision ID: c675ccd0f4e3
Revises: 52fff87b7e27
Create Date: 2019-07-11 16:17:00.207816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c675ccd0f4e3'
down_revision = '52fff87b7e27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('timestamps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stamp_type', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_timestamps_timestamp'), 'timestamps', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_timestamps_timestamp'), table_name='timestamps')
    op.drop_table('timestamps')
    # ### end Alembic commands ###
