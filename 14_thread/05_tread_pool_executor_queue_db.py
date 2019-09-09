from concurrent.futures import ThreadPoolExecutor
from queue import Queue
from random import choice
from threading import Lock

from requests_html import HTMLSession

from db import Database


target_domain = 'http://seoshnik.top/'
db = Database()
queue = Queue()
locker = Lock()
session = HTMLSession()
scaned_urls = set()

def worker():
    global scaned_urls
    # while not queue.empty():
    while queue.qsize():
        try:
            url = queue.get()

            if url in scaned_urls:
                continue

            # Wait by default 30sec / Wait 2 sec and send new request session.get(url, timeout=2)
            response = session.get(url)

            title = response.html.xpath('//title/text()')[0]

            with locker:
                # Add url to scaned_urs set
                scaned_urls.add(url)

                # with open('res_treads_2.txt', 'a') as f:
                #     f.write(title.strip() + '\n')

                db.insert([{'title': title.strip(), 'url': url}])

            # Set of all page links
            all_page_links = response.html.absolute_links

            # Add to queue ONLY not scaned links
            # https://stackoverflow.com/a/14545264
            [queue.put(link) for link in all_page_links if link not in scaned_urls and target_domain in link]

        except Exception as e:
            print('New request!', e)


def main():
    r = session.get(target_domain)

    # Add url to scaned_urs set
    scaned_urls.add(target_domain)

    title = r.html.xpath('//title/text()')[0]

    all_links = r.html.absolute_links

    # Add to queue ONLY not scaned links
    # https://stackoverflow.com/a/14545264
    [queue.put(link) for link in all_links if link not in scaned_urls and target_domain in link]

    with ThreadPoolExecutor(max_workers=10) as executor:
        for _ in range(10):
            executor.submit(worker)


if __name__ == "__main__":
    main()
