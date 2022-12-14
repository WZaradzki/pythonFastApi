"""Initial

Revision ID: 9279d69a5c89
Revises: 
Create Date: 2022-11-17 13:54:59.705638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9279d69a5c89'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('name_index', 'roles', ['name'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('surname', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('role_id', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('email_index', 'users', ['email'], unique=False)
    op.create_index('name_surname_index', 'users', ['name', 'surname'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('name_surname_index', table_name='users')
    op.drop_index('email_index', table_name='users')
    op.drop_table('users')
    op.drop_index('name_index', table_name='roles')
    op.drop_table('roles')
    # ### end Alembic commands ###
