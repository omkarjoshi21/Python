# Python Assessment 2 — Notes & Practical Programs

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

## Program Files

- [`oop_programs.py`](oop_programs.py) — Section 1 (Topics 2.1, 2.2, 2.3)
- [`modules_packages_asyncio.py`](modules_packages_asyncio.py) — Section 2 (Topics 3.3, 3.4)
- [`calc_pkg/`](calc_pkg/) — User-defined regular package (`__init__.py` + `ops.py`)
- [`ns_pkg/`](ns_pkg/) — User-defined namespace package (without `__init__.py`)
- [`exceptions_and_threads.py`](exceptions_and_threads.py) — Section 3 (Topics 6.1, 6.2)

---

### 2.1 Class, Object, Method Call, and Accessing Class Members

* **What is a Class?** Think of a class like a cookie cutter or a form template. If you make a `Student` class, it just says: "Every student has a `name` and `marks`." It does not hold one real student's data by itself.
* **What is an Object?** An object is one real item made from that template. For example, `s1 = Student("Riya", 85)` creates an actual student object named `s1`.
* **What is a Method Call?** A method is just a function written inside a class. Calling a method means asking that specific object to do something using a dot, like `s1.show_details()`.
* **How do you access class members outside the class?** Once you have an object `obj` (or the class name `Student`), you use a dot `.` to read or change variables or call methods outside the class—for example, `s1.name` or `Student.college`.

```python
class Student:
    college = "My College"  # Shared by all Student objects

    def __init__(self, name, marks):
        self.name = name    # Stored inside this specific object
        self.marks = marks  # Stored inside this specific object

    def show_details(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


# Create one object from the Student class
s1 = Student("Riya", 85)

# Access a variable outside the class using a dot
print("Outside access - Name:", s1.name)
print("Outside access - College:", Student.college)

# Call a method on the object
s1.show_details()
```

---

### 2.2 Setter and Getter Methods

* **What is a Getter method?** A getter is a method that **reads and returns** a variable's value instead of letting outside code grab it directly.
* **What is a Setter method?** A setter is a method that **updates** a variable's value—usually after checking an `if` condition so bad values (like negative age or negative marks) are blocked.

```python
class Person:
    def __init__(self, age):
        self._age = 0       # Start with a safe default
        self.set_age(age)   # Validate using the setter

    def get_age(self):
        return self._age    # Returns the stored age

    def set_age(self, new_age):
        if new_age >= 0:
            self._age = new_age
            print("Age set to:", self._age)
        else:
            print("Age cannot be negative. Keeping:", self._age)


p = Person(20)
print("Current age:", p.get_age())

p.set_age(-5)   # Blocked by if/else
p.set_age(21)   # Accepted
print("Final age:", p.get_age())
```

---

### 2.3 Constructor and Destructor

* **What is a Constructor (`__init__`)?** A special method that runs **automatically** the moment you create an object. Its job is to put starting values into the object (`self.name = ...`).
* **What is a Destructor (`__del__`)?** A special method that runs **automatically** when an object is destroyed or deleted with `del`. It is meant for cleanup messages or releasing resources.

```python
class Book:
    def __init__(self, title):
        self.title = title
        print("Constructor ran: Book created ->", self.title)

    def __del__(self):
        print("Destructor ran: Book removed ->", self.title)


b = Book("Python Basics")
print("Using book:", b.title)

del b  # Deletes the object and triggers __del__
```

---

### 3.3 Modules, Namespaces, Reloading, `math`, `random`, `datetime`, `map`, `filter`, `reduce`

* **What is a Module?** A single `.py` file containing ready-made functions or variables that you can bring into your program using `import`.
* **What is a Namespace?** A namespace is like a labeled box or folder of names so two things with the same name do not clash. For example, `math.pi` lives inside the `math` namespace.
* **What is Reloading a Module?** If you import a module and later change its code while your Python program/session is still running, `import` alone will not re-read the file. `importlib.reload(module_name)` forces Python to reload it.
* **Built-in modules (`math`, `random`, `datetime`):**
  * `math`: Math functions like square root (`math.sqrt`) and floor/ceil.
  * `random`: Generating random numbers or picking random items (`random.randint`, `random.choice`).
  * `datetime`: Working with today's date and current time (`datetime.datetime.now()`).
* **`map`, `filter`, `reduce`:**
  * `map(func, list)`: Applies `func` to **every** item and gives back transformed items.
  * `filter(func, list)`: Keeps **only** the items where `func` returns `True`.
  * `reduce(func, list)` (from `functools`): Takes two items at a time and squashes the whole list down into **one** single result.

```python
import datetime
import functools
import importlib
import math
import random

# math, random, datetime
print("Sqrt of 49:", math.sqrt(49))
print("Random number 1 to 10:", random.randint(1, 10))
print("Now:", datetime.datetime.now())

# Reloading a module
math = importlib.reload(math)

# map, filter, reduce with simple functions
numbers = [2, 5, 8, 11]


def add_ten(x):
    return x + 10


def is_even(x):
    return x % 2 == 0


def multiply(a, b):
    return a * b


plus_ten = list(map(add_ten, numbers))
even_nums = list(filter(is_even, numbers))
product_all = functools.reduce(multiply, numbers)

print("map (+10):", plus_ten)
print("filter (even):", even_nums)
print("reduce (multiply all):", product_all)
```

---

### 3.4 Packages, Namespace Packages, User-Defined Modules & Packages, and `asyncio`

* **What is a Package?** A folder that groups related `.py` module files together. A regular package has an `__init__.py` file inside the folder.
* **What is a Namespace Package?** A package folder **without** an `__init__.py` file. Python can combine folders with the same name across different locations into one package.
* **User-Defined Module & Package:** You create your own `.py` file (a module) or your own folder of `.py` files (a package) and import functions from it into your main script.

```text
Assessment 2/
├── modules_packages_asyncio.py
├── calc_pkg/
│   ├── __init__.py
│   └── ops.py
└── ns_pkg/
    └── notes.py
```

`calc_pkg/ops.py`:

```python
def add(a, b):
    return a + b
```

`modules_packages_asyncio.py`:

```python
from calc_pkg.ops import add

print(add(4, 6))
```

* **What is `asyncio`?** A way to run waiting tasks (like network calls or timers) without freezing the whole program. You mark a function with `async def`, use `await` when waiting on an async task, and run it with `asyncio.run(...)`.

```python
import asyncio


async def download_file(file_name, seconds):
    print("Downloading:", file_name)
    await asyncio.sleep(seconds)  # Waits without blocking other async tasks
    print("Done:", file_name)


async def main():
    t1 = asyncio.create_task(download_file("notes.pdf", 1))
    t2 = asyncio.create_task(download_file("slides.pptx", 1))
    await t1
    await t2


asyncio.run(main())
```

---

### 6.1 Exception Handling (`try`, `except`, `finally`, `raise`)

* **What is an Exception?** An error that happens while a program is running (like dividing by zero or typing `"abc"` instead of a number).
* **`try`:** Put risky code here.
* **`except`:** Runs if an error happens in `try`, letting you print a friendly message instead of crashing.
* **`finally`:** Always runs at the end—whether an error happened or not.
* **`raise`:** You force an error to happen on purpose when a condition is wrong (for example, marks less than 0).

```python
def check_marks(marks):
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")
    print("Valid marks:", marks)


try:
    score = int("90")
    check_marks(score)
except ValueError as error:
    print("Caught an error:", error)
finally:
    print("Finally block always runs.")
```

---

### 6.2 Multithreading (`sleep()` and `join()`)

* **What is Multithreading?** Running more than one path of execution (thread) inside a program so tasks can take turns or overlap while waiting.
* **`time.sleep(seconds)`:** Pauses the current thread for `seconds` seconds.
* **`thread.join()`:** Makes the main program wait until that thread finishes before moving on.

```python
import threading
import time


def print_numbers(label):
    for i in range(1, 4):
        print(label, "->", i)
        time.sleep(0.5)


t1 = threading.Thread(target=print_numbers, args=("Thread 1",))
t2 = threading.Thread(target=print_numbers, args=("Thread 2",))

t1.start()
t2.start()

t1.join()  # Wait for Thread 1 to finish
t2.join()  # Wait for Thread 2 to finish

print("Both threads finished.")
```
