import threading
import time

def thread_function(name):
    print(name)
    time.sleep(2)

if __name__ == "__main__":

    x = threading.Thread(target=thread_function, args=("haha",))
    y = threading.Thread(target=thread_function, args=("han",))
    x.start()
    y.start()

    x.join()
    y.join()