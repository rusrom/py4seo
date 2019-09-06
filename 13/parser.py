from pprint import pprint
from re import search, sub
from urllib.parse import urlparse, parse_qs

from requests_html import HTMLSession

from db import dsn, sa, vacancies


session = HTMLSession()
# resp = session.get('https://jobs.dou.ua/vacancies/?city=%D0%9A%D0%B8%D0%B5%D0%B2&category=Python')
resp = session.get('https://jobs.dou.ua/vacancies/?category=Blockchain')

url_structure = urlparse(resp.url)
category = parse_qs(url_structure.query)['category'][0]

jobs_list = resp.html.xpath('//div[@id="vacancyListId"]//li[contains(@class, "l-vacancy")]')

results = []
for job in jobs_list:
    data = {
        'url': job.xpath('.//div[@class="title"]/a[@class="vt"]/@href')[0].strip(),
        'title': job.xpath('.//div[@class="title"]/a[@class="vt"]/text()')[0].strip(),
        'description': job.xpath('.//div[@class="sh-info"]/text()[normalize-space()]')[0].strip(),
        'company': job.xpath('.//div[@class="title"]//a[@class="company"]/text()')[0].strip(),
        'category': category,
    }
    vacancy_id = search(r'vacancies/(\d+)', data['url'])
    company_vacancies = sub(r'(?<=vacancies\/).+', '', data['url'])
    city = job.xpath('.//div[@class="title"]/span[@class="cities"]/text()')
    
    data['company_vacancies'] = company_vacancies
    data['city'] = city[0].strip() if city else None
    data['vacancy_id'] = int(vacancy_id.group(1)) if vacancy_id else None
    data['hot'] = 1 if 'list_hot' in data['url'] else 0
    results.append(data)


# Save to database
engine = sa.create_engine(dsn)
conn = engine.connect()
conn.execute(vacancies.insert(), results)
