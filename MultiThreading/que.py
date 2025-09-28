import threading
import time
import random
from queue import Queue

counter = Queue(maxsize=6)

def chef():
    for i in range(10):
        dish = f"Dish- {i+1}"
        counter.put(dish)
        print(f"Chef prepared {dish}")
        time.sleep(random.uniform(0.5, 1.5))  # simulate time taken to prepare a dish

def waiter():
    for i in range(10):
        dish = counter.get()
        print(f"Waiter served {dish}")
        counter.task_done()
        time.sleep(random.uniform(1, 2))

t1 = threading.Thread(target=chef)
t2 = threading.Thread(target=waiter)

t1.start()
t2.start()

t1.join()
t2.join()

print("All dishes served!")