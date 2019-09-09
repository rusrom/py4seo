import sqlalchemy as sa


CONNECTION = {
    'user': 'py4seo',
    'database': 'python4seo',
    'host': 'localhost',
    'password': '1234567890',
}
DSN = 'mysql+pymysql://{user}:{password}@{host}/{database}'.format(**CONNECTION)


class Database:
    def __init__(self):
        self.metadata = sa.MetaData()
        self.seoshnik = sa.Table(
            'seoshnik', self.metadata,
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('title', sa.Text),
            sa.Column('url', sa.Text),
        )
        self.engine = sa.create_engine(DSN)
        # self.conn = self.engine.connect()

    def create_table(self):
        conn = self.engine.connect()
        # self.metadata.create_all(self.engine)
        # self.metadata.create_all(self.conn)
        self.metadata.create_all(conn)

    def insert(self, list_data_dicts):
        conn = self.engine.connect()
        # self.conn.execute(self.seoshnik.insert(), list_data_dicts)
        conn.execute(self.seoshnik.insert(), list_data_dicts)


if __name__ == '__main__':
    db = Database()
    # db.create_table()
    db.insert([
        {'title': 'Where ara my fish?', 'url':'url_1'},
        {'title': 'WPy4Seo', 'url':'url_2'},
        {'title': 'Chikas', 'url':'url_3'},
    ])
