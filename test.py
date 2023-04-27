from multiprocessing import Process
import time


def f(name):
    print('hello', name)
    time.sleep(5)


if __name__ == '__main__':
    p = Process(target=f, args=('bob', 'asdf', 'qwer'))
    p.start()
    p.join()
