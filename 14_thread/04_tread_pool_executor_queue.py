from requests_html import HTMLSession
from random import choice
from queue import Queue
from concurrent.futures import ThreadPoolExecutor


target_domain = 'http://seoshnik.top/'
session = HTMLSession()
scaned_urls = set()

def worker(queue):
    while not queue.empty():
        try:
            url = queue.get()
            if url in scaned_urls:
                continue

            # Wait by default 30sec / Wait 2 sec and send new request session.get(url, timeout=2)
            response = session.get(url)

            # Add url to scaned_urs set
            scaned_urls.add(url)

            title = response.html.xpath('//title/text()')[0]
            print(title.strip() + '\n' + url)

            # Get all page links
            all_page_links = response.html.absolute_links

            # Add all scraped links to queue
            # https://stackoverflow.com/a/31987220
            # map(queue.put, all_page_links)

            # Add ONLY not scaned links
            # https://stackoverflow.com/a/14545264
            [queue.put(link) for link in all_page_links if link not in scaned_urls and target_domain in link]

        except:
            print('New request!')


def main():
    queue = Queue()

    r = session.get(target_domain)

    # Add url to scaned_urs set
    scaned_urls.add(target_domain)

    title = r.html.xpath('//title/text()')[0]
    print(title.strip() + '\n' + target_domain)

    all_links = r.html.absolute_links

    # Add all scraped links to queue
    # https://stackoverflow.com/a/31987220
    # map(queue.put, all_page_links)

    # Add ONLY not scaned links
    # https://stackoverflow.com/a/14545264
    [queue.put(link) for link in all_links if link not in scaned_urls and target_domain in link]

    with ThreadPoolExecutor(max_workers=10) as pool:
        for _ in range(10):
            pool.submit(worker, queue)


if __name__ == "__main__":
    main()
