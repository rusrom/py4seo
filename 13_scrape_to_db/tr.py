import random
from time import sleep
from threading import Lock
from queue import Queue
from requests_html import HTMLSession
from concurrent.futures import ThreadPoolExecutor
from reppy.robots import Robots

# This utility uses `requests` to fetch the content

DOMAIN = 'goodreads.com'

scaned_urls = set()
locker = Lock()

robots = Robots.fetch(f'https://www.{DOMAIN}/robots.txt')


def worker(queue):
	session = HTMLSession()
	while True:
		if queue.qsize() == 0:
			sleep(30)
			if queue.qsize() == 0:
				break
		try:
			url = queue.get()
			print('Send request to', url)
			resp = session.get(url)
			title = resp.html.xpath('//title/text()')[0].strip()
			print(title)

			with locker:
				with open('my_file2.csv', 'a') as f:
					f.write(f'{url}\t{title}\n')

				for link in resp.html.absolute_links:
					if link in scaned_urls:
						continue
					elif DOMAIN not in link:
						continue
					else:
						if robots.allowed(link, '*'):
							queue.put(link)
							scaned_urls.add(link)
		except Exception as e:
			print(type(e), e)


def main():
	qu = Queue()
	url = f'http://{DOMAIN}/'
	session = HTMLSession()
	resp = session.get(url)
	
	for link in resp.html.absolute_links:
		print(robots.allowed(link, '*'), link)
		if robots.allowed(link, 'Googlebot'):
			qu.put(link)
			scaned_urls.add(link)

	print('Queue size', qu.qsize())

	with ThreadPoolExecutor(max_workers=50) as ex:
		for _ in range(50):
			ex.submit(worker, qu)


if __name__ == '__main__':
	main()
