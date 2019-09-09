from concurrent.futures import ThreadPoolExecutor
from queue import Queue
from random import choice
from threading import Lock
from pprint import pprint

from requests_html import HTMLSession

from db import Database


target_domain = 'http://seoshnik.top/'
db = Database()
queue = Queue()
locker = Lock()
session = HTMLSession()
scaned_urls = set()


def add_to_queue(links):
    # for link in links:
    #     if link not in scaned_urls and target_domain in link:
    #         scaned_urls.add(link)
    #         queue.put(link)

    # Equvivalent realization:
    # Add to queue ONLY not scaned links
    # https://stackoverflow.com/a/14545264
    [
        (scaned_urls.add(link), queue.put(link))
        for link in links
        if link not in scaned_urls and target_domain in link
    ]


def worker():
    while not queue.empty():
    # while queue.qsize():

        url = queue.get()

        try:
            response = session.get(url)

            title = response.html.xpath('//title/text()')[0]
            all_page_links = response.html.absolute_links

            with locker:
                # with open('res_treads.csv', 'a') as f:
                #     f.write(title.strip() + '\n')
                
                db.insert([{'title': title.strip(), 'url': url}])
                add_to_queue(all_page_links)

        except Exception as e:
            print('New request!', e)


def main():
    r = session.get(target_domain)
    all_links = r.html.absolute_links

    add_to_queue(all_links)

    with ThreadPoolExecutor(max_workers=10) as executor:
        for _ in range(10):
            executor.submit(worker)


if __name__ == "__main__":
    main()
