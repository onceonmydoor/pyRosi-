import threading
import random
import time
gMoney =0
gLock =threading.Lock()
gTotalTime = 10
gTimes =0
class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while True:
            gLock.acquire()
            Money=random.randint(1,100)
            if gTimes >= gTotalTime:
                gLock.release()
                break
            gMoney += Money
            print('%s生产了%d元钱，剩余%d元钱' % (threading.current_thread(),Money,gMoney))
            gTimes += 1
            gLock.release()
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(1,100)
            gLock.acquire()
            if gMoney >= money:
                gMoney -= money


                print('%s花费了%d元钱，剩余%d元钱' % (threading.current_thread(), money, gMoney))
            else:
                if gTimes >= gTotalTime:
                    gLock.release()

                    print('%s消费者准备消费%d元钱,但是只剩余%d元，钱不够了QAQ'% (threading.current_thread(), money, gMoney))
                    break
            gLock.release()
            time.sleep(0.5)

def main():
    for x in range(3):
        t = Producer(name="生产者线程%d"%x)
        t.start()

    for x in range(2):
        t = Consumer(name="消费者线程%d"%x)
        t.start()

if __name__ == '__main__':
    main()