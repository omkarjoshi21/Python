# Section 3: Exception Handling and Multithreading (6.1, 6.2)
# Study and revision examples with clear comments for beginners.

import threading
import time


# ---------------------------------------------------------
# 6.1 Exception Handling: try, except, finally, raise
# ---------------------------------------------------------
# - try: Code that might cause an error.
# - except: Code that runs if an error happens.
# - finally: Code that ALWAYS runs (error or no error).
# - raise: Manually trigger an error when a rule is broken.

def divide_numbers(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        answer = a / b
        print("Result:", answer)
    except ZeroDivisionError as err:
        print("Error caught:", err)
    except TypeError:
        print("Error caught: Please enter numbers only.")
    finally:
        print("Finally block: Division attempt finished.\n")


def check_age(age):
    try:
        if age < 0:
            raise ValueError("Age cannot be negative!")
        elif age < 18:
            print("Age", age, "-> Minor")
        else:
            print("Age", age, "-> Adult")
    except ValueError as err:
        print("Validation error:", err)


print("=== 6.1 Exception Handling ===")
divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, "a")

check_age(20)
check_age(-5)


# ---------------------------------------------------------
# 6.2 Multithreading: sleep(), join(), and Synchronization
# ---------------------------------------------------------
# - Thread: A separate flow of execution running inside a program.
# - time.sleep(sec): Pauses the current thread for given seconds.
# - thread.join(): Makes the main program wait until the thread finishes.
# - Lock: Prevents two threads from changing shared data at the same time.

counter = 0
lock = threading.Lock()


def print_task(task_name):
    for step in range(1, 4):
        print(task_name, "- step", step)
        time.sleep(0.3)  # Pause briefly


def add_to_counter(times):
    global counter
    for _ in range(times):
        lock.acquire()      # Lock before modifying shared variable
        counter = counter + 1
        lock.release()      # Release lock when done


print("\n=== 6.2 Multithreading (sleep & join) ===")
t1 = threading.Thread(target=print_task, args=("Thread-A",))
t2 = threading.Thread(target=print_task, args=("Thread-B",))

# Start both threads
t1.start()
t2.start()

# Wait for both threads to finish before moving on
t1.join()
t2.join()
print("Both print threads finished!")

print("\n=== 6.2 Thread Synchronization with Lock ===")
c1 = threading.Thread(target=add_to_counter, args=(1000,))
c2 = threading.Thread(target=add_to_counter, args=(1000,))

c1.start()
c2.start()

c1.join()
c2.join()
print("Final synchronized counter value:", counter)
