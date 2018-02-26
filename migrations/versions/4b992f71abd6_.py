"""empty message

Revision ID: 4b992f71abd6
Revises: 89d4dd37fd03
Create Date: 2018-02-26 20:28:25.789690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b992f71abd6'
down_revision = '89d4dd37fd03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('password', sa.String(length=255), nullable=True))
    op.create_unique_constraint(None, 'user_profile', ['password'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_profile', type_='unique')
    op.drop_column('user_profile', 'password')
    # ### end Alembic commands ###