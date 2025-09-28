import threading
import time
import random

#semaphaore allows only 3 threads at once
atm_semaphore = threading.Semaphore(2)

def use_atm(person):
    print(f"{person} is waiting to use the ATM...")
    with atm_semaphore: # only 2 people can access the ATM at once
        print(f" {person} is using the ATM...")
        time.sleep(random.randint(2, 4)) # simulate time taken to use ATM#  
        print(f" {person} has finished and left the ATM.")

# create 4 people
people = [threading.Thread(target=use_atm, args=(f"person {i}",)) for i in range(1, 5)]

# start all threads
for p in people:
    p.start()

# wait for all threads to finish
for p in people:
    p.join()

print("All people have used the ATM.")