import threading, time
barrier = threading.Barrier(3)

def friend(name):
    print(f"{name} is on the way...")
    time.sleep(2)
    print(f"{name} arrived")
    barrier.wait()  # wait for other friends
    print(f"{name} is starts eating...!")

for n in [" sanmesh", " pritam", " pratik"]:
    threading.Thread(target=friend, args=(n,)).start()


#2] example 

import threading
import time
import random

barrier = threading.Barrier(6)

def runner(name):
    print(f"{name} is warming up...")
    time.sleep(random.randint(1, 3))
    print(f"{name} reached the starting line")

    barrier.wait()  # wait for other runners
threads =[threading.Thread(target=runner, args=(f" runner {i+1}",)) for i in range(6)]

for t in threads:
    t.start()

for t in threads:
    t.join()