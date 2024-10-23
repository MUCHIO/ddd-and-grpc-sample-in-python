"""Insert route data

Revision ID: dd533b980f28
Revises: 03e20d5a0533
Create Date: 2024-10-23 16:50:03.743645

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision: str = 'dd533b980f28'
down_revision: Union[str, None] = '03e20d5a0533'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    with open('src/infrastructure/database/data/route_inserts.sql', 'r') as file:
        sql = file.read()

    op.execute(text(sql))

def downgrade() -> None:
    op.execute(text("DELETE FROM route;"))
