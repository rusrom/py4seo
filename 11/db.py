import sqlalchemy as sa


metadata = sa.MetaData()
connection = {
    'user': 'py4seo',
    'database': 'python4seo',
    'host': 'localhost',
    'password': '1234567890',
}
dsn = 'mysql+pymysql://{user}:{password}@{host}/{database}'.format(**connection)

Book = sa.Table(
    'books', metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('original_id', sa.Integer),
    sa.Column('name', sa.String(255)),
    sa.Column('description', sa.Text),
    sa.Column('book_details', sa.Text),
    sa.Column('comments', sa.Text),
    sa.Column('pages_num', sa.Integer),
    sa.Column('genres', sa.String(255)),
    sa.Column('alias', sa.String(255)),
    sa.Column('image', sa.String(255)),
    sa.Column('date', sa.Date),
    sa.Column('processed', sa.Boolean),
)

if __name__ == "__main__":
    engine = sa.create_engine(dsn)
    # metadata.drop_all(engine)
    metadata.create_all(engine)
