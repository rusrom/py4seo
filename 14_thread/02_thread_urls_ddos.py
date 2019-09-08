from threading import Thread
from requests_html import HTMLSession
from random import choice


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

# -----------------------------------+
# 1st variant for running 10 threads |
# -----------------------------------+

# thread_1 = Thread(target=worker)
# thread_2 = Thread(target=worker)
# thread_3 = Thread(target=worker)
# thread_4 = Thread(target=worker)
# thread_5 = Thread(target=worker)
# thread_6 = Thread(target=worker)
# thread_7 = Thread(target=worker)
# thread_8 = Thread(target=worker)
# thread_9 = Thread(target=worker)
# thread_10 = Thread(target=worker)


# thread_1.start()
# thread_2.start()
# thread_3.start()
# thread_4.start()
# thread_5.start()
# thread_6.start()
# thread_7.start()
# thread_8.start()
# thread_9.start()
# thread_10.start()


# -----------------------------------+
# 1st variant for running 10 threads |
# -----------------------------------+
for _ in range(10):
    thread = Thread(target=worker)
    thread.start()
