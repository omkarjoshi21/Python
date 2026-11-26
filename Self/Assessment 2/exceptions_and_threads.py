# Section 3: Exception Handling and Multithreading (6.1, 6.2)

import threading
import time


# ---------------------------------------------------------
# 6.1 Exception Handling (try, except, finally, raise)
# ---------------------------------------------------------
# try: Put risky code here.
# except: Runs if an error happens in try.
# finally: Always runs at the end, error or not.
# raise: Force an error on purpose when a condition is wrong.

def check_marks(marks):
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")
    print("Valid marks:", marks)


print("=== 6.1 Exception Handling ===")
try:
    score = int("90")
    check_marks(score)
except ValueError as error:
    print("Caught an error:", error)
finally:
    print("Finally block always runs.")


# ---------------------------------------------------------
# 6.2 Multithreading (sleep() and join())
# ---------------------------------------------------------
# time.sleep(seconds): Pauses the current thread for given seconds.
# thread.join(): Makes the main program wait until that thread finishes.

def print_numbers(label):
    for i in range(1, 4):
        print(label, "->", i)
        time.sleep(0.5)


print("\n=== 6.2 Multithreading ===")
t1 = threading.Thread(target=print_numbers, args=("Thread 1",))
t2 = threading.Thread(target=print_numbers, args=("Thread 2",))

t1.start()
t2.start()

t1.join()  # Wait for Thread 1 to finish
t2.join()  # Wait for Thread 2 to finish

print("Both threads finished.")
