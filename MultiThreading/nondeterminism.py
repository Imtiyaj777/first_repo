import threading, time

def print_numbers():
    for i in range(1, 11):
        print(i)
        time.sleep(0.5)

def print_alphabets():
    for char in 'abcdefghijk':
        print(char)
        time.sleep(1)
    
if __name__ =="__main__":
    num = threading.Thread(target=print_numbers, name="number-thread")
    char = threading.Thread(target=print_alphabets, name="alphabet-thread")

    num.start()
    char.start()

    num.join()
    num.join()



# create three function customer, waiter, chef and run them using threading

# import threading, time

# def customer_order():
#     for cus in ("biryani"):
#         print(cus)
#         time.sleep(2)

# def waiter_get_order():
#     for waiter in 'chef order of biryani':
#         print(waiter)
#         time.sleep(10)

# def chef():
#     for chef in 'order ready':
#         print(chef)
#         time.sleep(15)

# customer_order()
# waiter_get_order()
# chef()

# print("done")


# create function customer, waiter, chef and customer will place order and waiter will take order to chef 
# and chef will prepare the order and give it to waiter and waiter will give it to customer using threading

import threading, time 
def customer():
    print("customer: take my order")
    time.sleep(2)
    print("waiter: yes sir...!")
    time.sleep(2)
    print("customer: i want biryani, kabab and one water bottle")
    time.sleep(2)
    print("waiter: ok sir...!")
    time.sleep(2)

def waiter():
    print("waiter: order given to chef")
    time.sleep(2)
    print("chef: order received from waiter")
    time.sleep(2)
    print("waiter: customer order want on the one time")
    time.sleep(2)
    print("chef: ok...!")
    time.sleep(2)

def chef():
    print("chef: order is preparing")
    time.sleep(10)
    print("chef: order is ready")
    time.sleep(2)
    print("waiter: order is delivered to customer")
    time.sleep(2)
    print("customer: thank you...!")
    time.sleep(2)

c = threading.Thread(target=customer)
w = threading.Thread(target=waiter)
ch = threading.Thread(target=chef)
c.start()
w.start()
ch.start()
c.join()
w.join()
ch.join()