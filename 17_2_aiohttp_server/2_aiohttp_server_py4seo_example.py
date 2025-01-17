import random
from aiohttp import web


students = '''Шулежко Игорь
Топчій Анна Сергіївна
Вадим Ивашкевич
Сергей Смушков
Станислав Крамаренко
Сагач Оксана
Загробская Елена
Вячеслав Ковалев
Кирилюк Константин Александрович
Гладкий Андрей
Александр Хамбир
Антон Золотобоев
Коробка Олеся Александровна
Александр Конивненко
Харитонов Эдуард Константинович
Владимир Шаров
Баньковский Игорь Олегович
Якименко Владислав Петрович
Дорошенко Роман Іванович
Ярыш Илья Игоревич
Сергей Логвин
Роман Казнадий
Виталий Собко'''.split('\n')


async def home(request):
    body = f'<h1>{random.choice(students)}</h1><h2>Добро пожаловать на курс!</h2>'
    return web.Response(text=body, content_type='text/html')


app = web.Application()

app.router.add_route('GET', '/', home)

web.run_app(app, host='127.0.0.1', port=8000)
