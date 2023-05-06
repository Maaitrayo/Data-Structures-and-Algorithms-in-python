import threading 
import time

from collections import deque

class Queue:
    def __init__(self) -> None:
        self.buffer = deque()
    
    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer)==0
     
    def size(self):
        return len(self.buffer)

def take_orders(orders):
    for order in orders:
        print(f'Placing order for {order}')
        q.enqueue(order)
        time.sleep(0.5)

def serve_order():
    try:
        while True:
            item = q.dequeue()
            print(f'Now serving : {item}')
            time.sleep(2)
    except Exception as err:
        print("[!] Serving Finished")

def exercise_1():
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=take_orders, args=(orders,))
    t2 = threading.Thread(target=serve_order)

    t1.start()
    t2.start()
    # t1.join()
    # t2.join()

if __name__ == '__main__':
    q = Queue()
    exercise_1()
    