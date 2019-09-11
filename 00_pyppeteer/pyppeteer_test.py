import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://kartochki-domana.com.ua/')
    await asyncio.sleep(3)
    await page.screenshot({'path': 'pyppeteer_example.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
