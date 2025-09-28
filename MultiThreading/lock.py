import threading
import time

seats = 1 
lock = threading.Lock()

def book_ticket(user):
    global seats
    print(f"{user} is trying to book ticket...")
    time.sleep(10)

    with lock:
        if seats > 0:
            print(f"seat booked successfully for {user}")
            seats = seats - 1
        else:
            print(f"sorry {user} no seats available")

t1 = threading.Thread(target=book_ticket, args=('pratik',))
t2 = threading.Thread(target=book_ticket, args=('pritam',))
t3 = threading.Thread(target=book_ticket, args=('pranav',))
t4 = threading.Thread(target=book_ticket, args=('sanmesh',))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()