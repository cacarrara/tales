from sqlalchemy import Column, ForeignKey, String, orm

from thales.db import NamedModel


class Book(NamedModel):
    __tablename__ = 'books'
    author_id = Column(String, ForeignKey('authors.id'))
    author = orm.relationship('Author', backref='books')


class Author(NamedModel):
    __tablename__ = 'authors'
