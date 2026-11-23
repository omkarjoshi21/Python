from threading import Thread
def task():
    print("Thread is running")

# Created thread
t=Thread(target=task)

# Start Thread
t.start()

# Waiting for completion
t.join()
print("Main Program Ends")