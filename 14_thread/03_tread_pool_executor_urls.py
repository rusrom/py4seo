from requests_html import HTMLSession
from random import choice
from concurrent.futures import ThreadPoolExecutor


urls = [
    'https://some-url.io',
    'https://some-url.io',
    'https://some-url.io',
    'https://some-url.io',
    'https://some-url.io',
    'https://some-url.io',
    'https://some-url.io',
]

def worker():
    session = HTMLSession()
    while True:
        try:
            url = choice(urls)
            # Wait by default 30sec
            # session.get(url)
            # Wait 2 sec and send new request
            session.get(url, timeout=2)
            print(url)
        except:
            print('New request!')


with ThreadPoolExecutor(max_workers=10) as pool:
    for _ in range(10):
        pool.submit(worker)
