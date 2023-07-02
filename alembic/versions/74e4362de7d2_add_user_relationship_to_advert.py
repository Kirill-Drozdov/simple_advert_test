"""Add user relationship to Advert

Revision ID: 74e4362de7d2
Revises: 12a8f6f4a927
Create Date: 2023-07-02 16:32:36.056578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74e4362de7d2'
down_revision = '12a8f6f4a927'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('advert', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_advert_user_id_user', 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('advert', schema=None) as batch_op:
        batch_op.drop_constraint('fk_advert_user_id_user', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
