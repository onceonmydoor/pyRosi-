from queue import Queue
import time
import threading
q = Queue(4)


# q.put(1)
# # q.put(2)
# # end =q.get()
# for x in range(4):
#     q.put(x)
# print(q.full())#判断队列是否满
# # print(end)
# # print(q.qsize())
# for x in range(4):
#     print(q.get())#先进先出的顺序取出数据

def set_value(q):
    index =0
    while True:
        q.put(index)
        index +=1
        time.sleep(3)
def get_value(q):
    while True:
        print(q.get(block=True))

def main():
    q =Queue(4)
    t1 = threading.Thread(target=get_value,args=[q])
    t2 = threading.Thread(target=set_value,args=[q])

    t1.start()
    t2.start()

if __name__ == '__main__':
    main()