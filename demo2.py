import threading
import time

VALUE=0

gLock =threading.Lock()
#锁线程
def add_value():
    global VALUE
    gLock.acquire()
    for x in range(1000000):
        VALUE +=1
    gLock.release()
    print(VALUE)


def main():
    for x in range(2):
        t =threading.Thread(target=add_value)
        t.start()


if __name__ == '__main__':
    main()