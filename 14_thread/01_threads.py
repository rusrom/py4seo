from threading import Thread


def worker_1():
    while True:
        print('Thread 1 is working .........')

trhread_1 = Thread(target=worker_1)
trhread_1.start()


def worker_2():
    while True:
        print('Thread 2 is working >>>>>>>>>')

trhread_2 = Thread(target=worker_2)
trhread_2.start()
