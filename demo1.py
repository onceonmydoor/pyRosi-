import threading
import time


class CodingThread(threading.Thread):
    def run(self):
        for x in range(10):
            print('fuck%s' % threading.current_thread())
            time.sleep(1)
class DrawingThread(threading.Thread):
    def run(self):
        for x in range(10):
            print('draw%s' % threading.current_thread())
            time.sleep(1)

def coding():
    for x in range(10):
        print('fuck%s'%x)
        time.sleep(1)
def drawing():
    for x in range(10):
        print('draw%s'%x)
        time.sleep(1)
def single_thread():
    coding()
    drawing()
def muli_thread():
    t1 =threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)

    t1.start()
    t2.start()
    print(threading.enumerate())


def main():
    t1 =CodingThread()
    t2 =DrawingThread()
    t1.start()
    t2.start()
if __name__ == '__main__':
# muli_thread()
        main()