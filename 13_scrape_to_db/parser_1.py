from requests_html import HTMLSession
from db import *


session = HTMLSession()

resp = session.get('https://seoprofy.ua/blog')

# links = resp.html.absolute_links
text = resp.html.text
title = resp.html.xpath('//title/text()')[0]
name = resp.html.xpath('//h1/text()')[0]

text = 'Наша маша громко плачет'
title = 'Блог Блог Блог'

engine = sa.create_engine(dsn)
conn = engine.connect()

# sql = Book.insert().values(description=text, name=name, book_details=title)

# sql = sa.text(f'INSERT INTO books_4e (description, name, book_details) VALUES ("{text}", "{name}", "{title}");')

# print(sql)

curs = conn.execute('select * from books_4e;')

for row in curs:
	print(row)


print('All done!')
