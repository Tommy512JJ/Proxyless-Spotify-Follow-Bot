from follow_bot import spotify
import threading

spotify_profile = "31cjkf4q4b4rl7o2wjuah2bnnn5y" #Link or username to profile
lock = threading.Lock()
threads = int(input("\nThreads: "))
counter = 0

def safe_print(arg):
    lock.acquire()
    print(arg)
    lock.release()

def thread_starter():
    global counter
    obj = spotify(spotify_profile)
    result = obj.follow()
    if result:
        counter += 1
        safe_print("Followed {}".format(counter))
    else:
        safe_print("Error")

while True:
    if threading.active_count() <= threads:
        try:
            threading.Thread(target = thread_starter).start()
        except:
            pass
