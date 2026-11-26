# Section 2: Modules, Packages, and Asyncio (3.3, 3.4)
# Study and revision examples with clear comments for beginners.

import math
import random
import datetime as dt
from functools import reduce
import importlib
import asyncio

# User-defined module and packages
import my_module
import my_pkg.helpers
from my_pkg.helpers import make_uppercase
import ns_pkg.notes


# ---------------------------------------------------------
# 3.3 Module Basic Usage, Namespaces, Built-in Modules,
#     map, filter, reduce, and Reloading Modules
# ---------------------------------------------------------

print("=== 3.3 Built-in Modules & Namespaces ===")
# Using 'math' namespace
print("Square root of 36:", math.sqrt(36))
print("Value of pi:", round(math.pi, 3))

# Using 'random' namespace
dice = random.randint(1, 6)
fruits = ["Apple", "Mango", "Banana"]
picked = random.choice(fruits)
print("Dice roll:", dice)
print("Random fruit:", picked)

# Using 'datetime' with alias 'dt'
today = dt.date.today()
print("Today's date:", today)

print("\n=== 3.3 map, filter, reduce ===")
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


# map() applies square() to each item
squared_list = list(map(square, numbers))

# filter() keeps items where is_even() returns True
even_list = list(filter(is_even, numbers))

# reduce() combines all items into one value
total = reduce(add, numbers)

print("Original:", numbers)
print("map()   :", squared_list)
print("filter():", even_list)
print("reduce():", total)

print("\n=== 3.3 User-Defined Module & Reloading ===")
my_module.greet("Omkar")

# Changing VERSION in memory, then reloading from disk
my_module.VERSION = "9.9-temp"
print("Modified VERSION in memory:", my_module.VERSION)

importlib.reload(my_module)
print("VERSION after importlib.reload():", my_module.VERSION)


# ---------------------------------------------------------
# 3.4 Packages, Namespace Packages, and Asyncio
# ---------------------------------------------------------

print("\n=== 3.4 Regular Package vs Namespace Package ===")
# Regular package (has __init__.py)
result = my_pkg.helpers.add_numbers(10, 20)
print("Sum from my_pkg.helpers:", result)
print("Uppercase from my_pkg.helpers:", make_uppercase("python"))

# Namespace package (no __init__.py)
print("Namespace package message:", ns_pkg.notes.get_note())
print("ns_pkg.__file__ is:", ns_pkg.__file__)


# Asyncio: running asynchronous tasks without blocking
async def download_file(file_name, seconds):
    print("Started:", file_name)
    await asyncio.sleep(seconds)  # Pauses this task without blocking others
    print("Finished:", file_name)


async def run_async_tasks():
    print("\n=== 3.4 Asyncio Basics ===")
    # asyncio.gather runs both tasks concurrently
    await asyncio.gather(
        download_file("Notes.pdf", 1),
        download_file("Slides.pptx", 1),
    )
    print("All async downloads complete!")


asyncio.run(run_async_tasks())
