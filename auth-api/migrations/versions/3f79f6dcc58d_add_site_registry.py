"""Add Site Registry product.

Revision ID: 3f79f6dcc58d
Revises: 1344cb533815
Create Date: 2022-07-20 20:25:08.709478

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3f79f6dcc58d'
down_revision = '1344cb533815'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    product_code_table = sa.sql.table('product_codes',
        sa.column('code', sa.String),
        sa.column('description', sa.String),
        sa.column('default', sa.Boolean),
        sa.column('type_code', sa.String),
        sa.column('hidden', sa.Boolean),
        sa.column('need_review', sa.Boolean),
        sa.column('premium_only', sa.Boolean)
    )

    op.bulk_insert(
        product_code_table,
        [
            {
                'code': 'ESRA', 'description': 'Site Registry', 'default': False, \
                'type_code': 'PARTNER', 'hidden': True, 'need_review': False, 'premium_only': True
            }
        ]
    )

    op.alter_column('activity_logs', 'item_value',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.String(length=900),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("DELETE FROM product_codes WHERE code in ('ESRA')")
    op.alter_column('activity_logs', 'item_value',
               existing_type=sa.String(length=900),
               type_=sa.VARCHAR(length=500),
               existing_nullable=True)
    # ### end Alembic commands ###
