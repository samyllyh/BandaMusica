"""empty message

Revision ID: 791829f33d41
Revises: 0f99a42bb988
Create Date: 2024-12-17 15:42:02.301678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '791829f33d41'
down_revision = '0f99a42bb988'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('endereco', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=255),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('endereco', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.String(length=255),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###