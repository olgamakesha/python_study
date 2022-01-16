from threading import Thread
from time import sleep

def thread_func(thread_number):
    print("run thread " + str(thread_number) + "\n")
    reversed_numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    for i in reversed_numbers:
        print(str(i) + " (thread number: " + str(thread_number) + ")\n")
        sleep(1)
    print("stop thread " + str(thread_number) + "\n")

first_thread = Thread(target=thread_func, args={1,})
second_thread = Thread(target=thread_func, args={2,})

first_thread.start()
second_thread.start()