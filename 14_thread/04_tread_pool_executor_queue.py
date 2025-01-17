from requests_html import HTMLSession
from random import choice
from queue import Queue
from threading import Lock
from concurrent.futures import ThreadPoolExecutor


target_domain = 'http://seoshnik.top/'
queue = Queue()
locker = Lock()
session = HTMLSession()
scaned_urls = set()

def worker():
    global scaned_urls
    while not queue.empty():
        try:
            with locker:
                url = queue.get()

            if url in scaned_urls:
                continue

            # Wait by default 30sec / Wait 2 sec and send new request session.get(url, timeout=2)
            response = session.get(url)

            # Add url to scaned_urs set
            with locker:
                scaned_urls.add(url)

            title = response.html.xpath('//title/text()')[0]
            # print(title.strip() + '\n' + url)
            print(title.strip())

            # Get all page links
            all_page_links = response.html.absolute_links

            # Add all scraped links to queue
            # https://stackoverflow.com/a/31987220
            # map(queue.put, all_page_links)

            # Add ONLY not scaned links
            # https://stackoverflow.com/a/14545264
            with locker:
                [queue.put(link) for link in all_page_links if link not in scaned_urls and target_domain in link]

        except Exception as e:
            print('New request!', e)


def main():
    r = session.get(target_domain)

    # Add url to scaned_urs set
    scaned_urls.add(target_domain)

    title = r.html.xpath('//title/text()')[0]
    # print(title.strip() + '\n' + target_domain)
    print(title.strip())

    all_links = r.html.absolute_links

    # Add all scraped links to queue
    # https://stackoverflow.com/a/31987220
    # map(queue.put, all_page_links)

    # Add ONLY not scaned links
    # https://stackoverflow.com/a/14545264
    [queue.put(link) for link in all_links if link not in scaned_urls and target_domain in link]

    with ThreadPoolExecutor(max_workers=10) as pool:
        for _ in range(10):
            pool.submit(worker)


if __name__ == "__main__":
    main()
