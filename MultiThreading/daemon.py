import threading
import time

#task 1: main app task (ordering food)
def place_order():
    print("order place successfully!")
    time.sleep(2)
    print("order confirmend!")

#task 2: backgraound logging (tracking delivery updates)
def background_logging():
    for i in range(5):
        time.sleep(1)   #simulating delay in logging
        print(f"logging delivery update... step {i+1}")

#creating threads
main_thread = threading.Thread(target=place_order)
background_thread = threading.Thread(target=background_logging, daemon=True)
#daemon=true means it runs in background and will not block app exit

#starting threads
main_thread.start()
background_thread.start()

#wait for main order process to complete
main_thread.join()
print("you can close the app now!, logging will not block app exit")

