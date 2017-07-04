"""Init

Revision ID: 7d8e82433848
Revises:
Create Date: 2017-07-03 16:18:09.925793+00:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7d8e82433848'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'authors',
        sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
        sa.Column('name', sa.String(length=200), nullable=True),
        sa.Column('slug', sa.String(length=256), nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_authors')),
        sa.UniqueConstraint('name', name=op.f('uq_authors_name')),
        sa.UniqueConstraint('slug', name=op.f('uq_authors_slug'))
    )
    op.create_table(
        'books',
        sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
        sa.Column('name', sa.String(length=200), nullable=True),
        sa.Column('slug', sa.String(length=256), nullable=True),
        sa.Column('author_id', postgresql.UUID(), nullable=True),
        sa.ForeignKeyConstraint(['author_id'], ['authors.id'], name=op.f('fk_books_author_id_authors')),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_books')),
        sa.UniqueConstraint('name', name=op.f('uq_books_name')),
        sa.UniqueConstraint('slug', name=op.f('uq_books_slug'))
    )


def downgrade():
    op.drop_table('books')
    op.drop_table('authors')
