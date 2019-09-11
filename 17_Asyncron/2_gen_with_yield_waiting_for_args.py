# Генератор который что то возвращает это просто ГЕНЕРАТОР
# Генератор получающий что то на вход называется КОРУТИНА

def calc():
    history = []
    while True:
        x, y, *z = yield
        if x == 'history':
            print(history)
            continue
        if z:
            print(f'Extra arguments: {z}')
        result = x * y
        print(result)
        history.append(result)

c = calc()

# Generator init
next(c) 

# Send values to generator
c.send((2, 4))
c.send((5, 6, 67, 98, 'test'))
c.send((7, 4))
c.send(('history', 3))
c.close()
