"""project_description

Revision ID: 96940833624b
Revises: 035147c7b56d
Create Date: 2023-09-25 01:09:34.491289

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96940833624b'
down_revision: Union[str, None] = '035147c7b56d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('description', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project', 'description')
    # ### end Alembic commands ###
