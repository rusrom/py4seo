import aiohttp
import asyncio
from pprint import pprint
from parsel import Selector
from concurrent.futures import ThreadPoolExecutor

# py4seo variant
# async def main():
#     session = aiohttp.ClientSession()
#     response = await session.get('http://python.org')
#     html = await response.text()
#     sel = Selector(text=html)
#     print(dir(sel))
#     await session.close()

domain = 'kartochki-domana.com.ua'
queue = asyncio.Queue()
added_prod_urls = set()

loop = asyncio.get_event_loop()
executor = ThreadPoolExecutor(max_workers=10)


def scrape_data(html):
    sel = Selector(text=html)
    title = sel.xpath('//h1[contains(@class, "product_title")]/text()').get()
    price = sel.xpath('//p[@class="price"]/span[contains(@class, "woocommerce-Price-amount")]/text()').get()
    return title, price

# My variant
async def worker(session):
    while not queue.empty():
        target_url = await queue.get()
        async with session.get(target_url) as response:
            html = await response.text()
        
        title, price = await loop.run_in_executor(executor, scrape_data, html)
        print(f'{title}: {price}')
        
        # [
        #     (await queue.put(prod_url), added_prod_urls.add(prod_url))
        #     for prod_url in prod_urls
        #     if prod_url not in added_prod_urls
        # ]


async def main(): 
    async with aiohttp.ClientSession() as session:
        response = await session.get('https://kartochki-domana.com.ua/ru/product-category/podarochnie-nabori/')
        html = await response.text()
        
        sel = Selector(text=html)
        prod_urls = sel.xpath('//h3[@class="product_title"]/a/@href').getall()

        [
            (await queue.put(prod_url), added_prod_urls.add(prod_url))
            for prod_url in prod_urls
            if prod_url not in added_prod_urls
        ]
        
        print(queue.qsize())
        # pprint(added_prod_urls)
        
        tasks = []
        for _ in range(50):
            task = asyncio.Task(worker(session))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == '__main__':


    # task1 = asyncio.Task(coro())
    # task2 = asyncio.Task(main())

    # runer = asyncio.gather(task1, task2)

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(runer)


    # Run just 1 coroutine main()
    
    loop.run_until_complete(main())
