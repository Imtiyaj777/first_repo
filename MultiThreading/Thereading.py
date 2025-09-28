#example : downloading 3 songs

import threading, time

def download_song(song_name):
    print(f"downloading....{song_name}")
    time.sleep(3)
    print(f"downloaded...!{song_name}")

# without threading
def normal_program():
    start = time.time()
    download_song("song1")
    download_song("song2")
    download_song("song3")
    end = time.time()
    print("time taken without threading", end - start)

normal_program()

#with threading
def thread_program():
    start1 = time.time()
    threads = []
    for song in ["song1", "song2", "song3"]:
        t = threading.Thread(target=download_song, args=(song,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    end1 = time.time()
    print("time taken with threading", end1 - start1)

thread_program()