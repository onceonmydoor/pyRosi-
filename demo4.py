import threading
import random
import time
gMoney =0
gCondition =threading.Condition()
gTotalTime = 10
gTimes =0
class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while True:
            gCondition.acquire()
            Money=random.randint(1,100)
            if gTimes >= gTotalTime:
                gCondition.release()
                break
            gMoney += Money
            print('%s生产了%d元钱，剩余%d元钱' % (threading.current_thread(),Money,gMoney))
            gTimes += 1
            gCondition.notify_all()
            gCondition.release()
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(1,100)
            gCondition.acquire()
            while gMoney < money:
                if gTimes > gTotalTime:
                    gCondition.release()
                    return
                print("%s消费了%d元钱,还剩%d元钱，钱不够了" % (threading.current_thread(), money, gMoney))
                gCondition.wait()#等通知，之后排队获取锁
            gMoney -= money
            print("%s消费了%d元钱,还剩%d元钱" % (threading.current_thread(),money,gMoney))
            gCondition.release()
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