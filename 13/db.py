import sqlalchemy as sa


metadata = sa.MetaData()
connection = {
    'user': 'py4seo',
    'database': 'python4seo',
    'host': 'localhost',
    'password': '1234567890',
}
dsn = 'mysql+pymysql://{user}:{password}@{host}/{database}'.format(**connection)


vacancies = sa.Table(
    'vacancies', metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('vacancy_id', sa.Integer),
    sa.Column('city', sa.String(255)),
    sa.Column('hot', sa.Boolean),
    sa.Column('company', sa.String(255)),
    sa.Column('title', sa.String(255)),
    sa.Column('description', sa.Text),
    sa.Column('url', sa.Text),
    sa.Column('company_vacancies', sa.Text),
    sa.Column('category', sa.String(255)),
    sa.Column('date', sa.Date),
    sa.Column('processed', sa.Boolean)
)


if __name__ == '__main__':
    engine = sa.create_engine(dsn)
    # metadata.drop_all(engine)
    metadata.create_all(engine)
