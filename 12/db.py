import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
Session = sessionmaker()

connection = {
    'user': 'py4seo',
    'database': 'python4seo',
    'host': 'localhost',
    'password': '1234567890',
}

dsn = 'mysql+pymysql://{user}:{password}@{host}/{database}'.format(**connection)
engine = sa.create_engine(dsn)

Base.metadata.bind = engine
Session.configure(bind=engine)
session = Session()

class Book(Base):
    __tablename__ = 'buklya_books'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255))
    author_id = sa.Column(sa.Integer, ForeignKey('buklya_authors.id'))
    author = relationship('Author', back_populates='books')
    # processed = sa.Column(sa.Boolean)


class Author(Base):
    __tablename__ = 'buklya_authors'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255))
    books = relationship('Book', back_populates='author')


if __name__ == "__main__":
    engine = sa.create_engine(dsn)
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
