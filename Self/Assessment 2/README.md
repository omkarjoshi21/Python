# Python Assessment 2 — Study Notes & Practical Programs

## Syllabus (Assessment 2)

1. **Object Oriented Programming**
   - **2.1** Concept of class, object, method call, accessing class members outside the class
   - **2.2** Setter and Getter methods
   - **2.3** Constructor and destructors
2. **Modules, Packages, and Asyncio**
   - **3.3** Module basic usage, namespaces, reloading modules — `math`, `random`, `datetime`, `map`, `filter`, `reduce`
   - **3.4** Package: import basics, namespace packages, user defined modules and packages, `asyncio`
3. **Exception Handling and Multithreading**
   - **6.1** Exception Handling: `try`, `except`, `finally`, `raise`
   - **6.2** Multithreading: synchronizing the threads — `sleep()`, `join()`

---

## Files in This Folder

- [`oop_programs.py`](oop_programs.py) — Section 1 (Topics 2.1, 2.2, 2.3)
- [`modules_packages_asyncio.py`](modules_packages_asyncio.py) — Section 2 (Topics 3.3, 3.4)
- [`my_module.py`](my_module.py) — User-defined module used in Section 2
- [`my_pkg/`](my_pkg/) — User-defined regular package (with `__init__.py`)
- [`ns_pkg/`](ns_pkg/) — User-defined namespace package (without `__init__.py`)
- [`exceptions_and_threads.py`](exceptions_and_threads.py) — Section 3 (Topics 6.1, 6.2)

---

## 1. Object Oriented Programming

### 2.1 Concept of Class, Object, Method Call, Accessing Class Members Outside the Class

- **Class**: A blueprint or template that defines what data (attributes) and actions (methods) an object will have.
- **Object**: A real instance created from a class. You can create many objects from one class.
- **Method**: A function defined inside a class. Its first parameter is `self`, which refers to the current object.
- **Accessing Members Outside the Class**: You can read or update attributes and call methods using dot notation (`object.attribute` or `object.method()`).

**Example Program** (from `oop_programs.py`):

```python
class Student:
    college = "IMCC"  # Class attribute

    def set_info(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def show_info(self):
        print("College :", Student.college)
        print("Name    :", self.name)
        print("Roll No :", self.roll_no)
        print("Marks   :", self.marks)

    def check_pass(self):
        if self.marks >= 40:
            print(self.name, "-> Pass")
        else:
            print(self.name, "-> Fail")


s1 = Student()
s2 = Student()

s1.set_info("Aarav", 101, 75)
s2.set_info("Diya", 102, 32)

s1.show_info()
s1.check_pass()

# Accessing and updating members outside the class
print("College accessed outside class:", Student.college)
s2.marks = 50
s2.check_pass()
```

### 2.2 Setter and Getter Methods

- **Getter Method**: A method used to safely read an attribute's value (for example, `get_balance()`).
- **Setter Method**: A method used to update an attribute's value with validation rules (for example, `set_balance(amount)` rejecting negative numbers).
- **Why use them?** They protect internal data (often named with a leading underscore like `_balance`) from invalid values.

**Example Program** (from `oop_programs.py`):

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = 0
        self.set_balance(balance)

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount < 0:
            print("Invalid amount! Balance cannot be negative.")
        else:
            self._balance = amount

    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self._balance + amount)
            print("Deposited:", amount)
        else:
            print("Deposit must be greater than 0.")


acc = BankAccount("Rohan", 1000)
print("Starting Balance:", acc.get_balance())
acc.deposit(500)
acc.set_balance(-200)  # Rejected by setter
print("Balance:", acc.get_balance())
```

### 2.3 Constructor and Destructor

- **Constructor (`__init__`)**: A special method that runs automatically as soon as a new object is created. It sets up initial values.
- **Destructor (`__del__`)**: A special method that runs automatically when an object is destroyed (via `del obj` or when the program ends).

**Example Program** (from `oop_programs.py`):

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        print("Constructor called -> Created book:", self.title)

    def display(self):
        print("Book:", self.title, "| Author:", self.author)

    def __del__(self):
        print("Destructor called -> Removed book:", self.title)


b1 = Book("Python Basics", "Guido")
b2 = Book("Clean Code", "Robert")
b1.display()
b2.display()
del b1
```

---

## 2. Modules, Packages, and Asyncio

### 3.3 Module Basic Usage, Namespaces, Reloading Modules (`math`, `random`, `datetime`, `map`, `filter`, `reduce`)

- **Module**: A `.py` file containing reusable functions, classes, and variables.
- **Namespace**: A separate space for names inside a module so two modules can have functions with the same name without clashing (e.g., `math.sqrt()`).
- **Built-in Modules**:
  - `math`: Mathematical functions like `math.sqrt()`, `math.pi`, `math.factorial()`.
  - `random`: Random values like `random.randint(1, 6)` and `random.choice(list)`.
  - `datetime`: Dates and times like `datetime.date.today()`.
- **Functional Helpers**:
  - `map(func, list)`: Applies `func` to every item and returns the results.
  - `filter(func, list)`: Keeps only items where `func` returns `True`.
  - `reduce(func, list)` (from `functools`): Combines all items into one final value.
- **Reloading Modules**: Python caches a module after the first `import`. `importlib.reload(module)` forces Python to re-read the module from disk.

**Example Program** (from `modules_packages_asyncio.py` and `my_module.py`):

```python
import math
import random
import datetime as dt
from functools import reduce
import importlib
import my_module

print("Square root of 36:", math.sqrt(36))
print("Dice roll:", random.randint(1, 6))
print("Today's date:", dt.date.today())

numbers = [1, 2, 3, 4, 5, 6]

def square(n):
    return n * n

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def add(a, b):
    return a + b

print("map()   :", list(map(square, numbers)))
print("filter():", list(filter(is_even, numbers)))
print("reduce():", reduce(add, numbers))

my_module.greet("Omkar")
my_module.VERSION = "9.9-temp"
importlib.reload(my_module)
print("VERSION after reload:", my_module.VERSION)
```

### 3.4 Package: Import Basics, Namespace Packages, User-Defined Modules and Packages, `asyncio`

- **Regular Package**: A folder containing Python modules and an `__init__.py` file. Imported using `import package.module` or `from package.module import name`.
- **Namespace Package**: A folder containing Python modules **without** an `__init__.py` file (supported in Python 3.3+). Its `__file__` attribute is `None`.
- **`asyncio`**: A built-in library for running tasks concurrently using `async def`, `await`, `asyncio.sleep()`, `asyncio.gather()`, and `asyncio.run()`. While one task waits (for example, `await asyncio.sleep(1)`), other tasks can run.

**Example Program** (from `modules_packages_asyncio.py`):

```python
import asyncio
import my_pkg.helpers
from my_pkg.helpers import make_uppercase
import ns_pkg.notes

print("Sum from my_pkg.helpers:", my_pkg.helpers.add_numbers(10, 20))
print("Uppercase:", make_uppercase("python"))
print("Namespace package:", ns_pkg.notes.get_note())
print("ns_pkg.__file__:", ns_pkg.__file__)

async def download_file(file_name, seconds):
    print("Started:", file_name)
    await asyncio.sleep(seconds)
    print("Finished:", file_name)

async def run_async_tasks():
    await asyncio.gather(
        download_file("Notes.pdf", 1),
        download_file("Slides.pptx", 1),
    )
    print("All async downloads complete!")

asyncio.run(run_async_tasks())
```

---

## 3. Exception Handling and Multithreading

### 6.1 Exception Handling: `try`, `except`, `finally`, `raise`

- **`try`**: Wrap code that might cause a runtime error.
- **`except`**: Catch and handle a specific error so the program does not crash.
- **`finally`**: A block that **always** runs at the end, whether an error happened or not (useful for cleanup).
- **`raise`**: Manually trigger an exception when a condition or rule is violated.

**Example Program** (from `exceptions_and_threads.py`):

```python
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

divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, "a")
```

### 6.2 Multithreading: Synchronizing Threads — `sleep()`, `join()`

- **Thread**: A lightweight unit of execution that lets a program run multiple tasks at the same time using the `threading` module.
- **`time.sleep(seconds)`**: Pauses the current thread for the given number of seconds.
- **`thread.join()`**: Tells the main program to wait until that thread finishes before continuing.
- **Synchronization (`threading.Lock`)**: Ensures only one thread at a time modifies a shared variable, preventing race conditions.

**Example Program** (from `exceptions_and_threads.py`):

```python
import threading
import time

counter = 0
lock = threading.Lock()

def print_task(task_name):
    for step in range(1, 4):
        print(task_name, "- step", step)
        time.sleep(0.3)

def add_to_counter(times):
    global counter
    for _ in range(times):
        lock.acquire()
        counter = counter + 1
        lock.release()

t1 = threading.Thread(target=print_task, args=("Thread-A",))
t2 = threading.Thread(target=print_task, args=("Thread-B",))
t1.start()
t2.start()
t1.join()
t2.join()

c1 = threading.Thread(target=add_to_counter, args=(1000,))
c2 = threading.Thread(target=add_to_counter, args=(1000,))
c1.start()
c2.start()
c1.join()
c2.join()
print("Final synchronized counter value:", counter)
```
