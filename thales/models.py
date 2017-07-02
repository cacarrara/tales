from sqlalchemy import Column, ForeignKey, orm
from sqlalchemy.dialects.postgresql import UUID

from thales.db import NamedModel


class Book(NamedModel):
    __tablename__ = 'books'
    author_id = Column(UUID, ForeignKey('authors.id'))
    author = orm.relationship('Author', backref='books')


class Author(NamedModel):
    __tablename__ = 'authors'
