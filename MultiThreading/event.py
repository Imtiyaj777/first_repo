import threading
import time

#event object (initially not set)
game_start = threading.Event()

def player(name):
    print(f"{name} has joined the lobby and is waiting for the race to start...")
    game_start.wait()  #wait until the event is set
    print(f"{name} started racing!")

def host():
    print("host is preparing the race....")
    time.sleep(5)  #simulate delay before host starts the game
    print("host press the start button!")
    game_start.set()  # signal all players to start

#create player threads
players = [threading.Thread(target=player, args=(f"Player-{i}",)) for i in range(1, 4)]

#start player threads
for p in players:
    p.start()

# host thread
threading.Thread(target=host).start()