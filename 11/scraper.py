from queue import Queue
from concurrent.futures import ThreadPoolExecutor
from requests_html import HTMLSession
from db import Book, sa, dsn


def worker(qu):
    engine = sa.create_engine(dsn)
    conn = engine.connect()
    session = HTMLSession()

    while qu.qsize() > 0:
        try:
            url = qu.get()
            resp = session.get(url)
            title = resp.html.xpath('//title/text()')[0]
            title = title.strip()
            conn.execute(Book.create().value(description=title))
            print(title)
            new_links = resp.html.absolute_links
            
            for ln in new_links:
                # qu.put(url)
                qu.put(ln)


        except Exception as e:
            print(type(e), e)

def main():
    domain = input('Enter domain name:')
    home_url = f'http://{domain}/'
    session = HTMLSession()

    q = Queue()
    resp = session.get(home_url)
    new_links = resp.html.absolute_links
    for ln in new_links:
        q.put(ln)
    
    print(q.qsize())
    executor = ThreadPoolExecutor(max_workers=10)
    for _ in range(10):
        executor.submit(worker, q)

main()
