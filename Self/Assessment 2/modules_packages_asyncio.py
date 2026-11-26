# Section 2: Modules, Packages, and Asyncio (3.3, 3.4)

import asyncio
import datetime
import functools
import importlib
import math
import random

# User-defined regular package and namespace package
from calc_pkg.ops import add
import ns_pkg.notes


# ---------------------------------------------------------
# 3.3 Modules, Namespaces, Reloading, math, random,
#     datetime, map, filter, reduce
# ---------------------------------------------------------

print("=== 3.3 Modules, Namespaces, Reloading ===")
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


# ---------------------------------------------------------
# 3.4 Packages, Namespace Packages, and Asyncio
# ---------------------------------------------------------

print("\n=== 3.4 Packages & Namespace Packages ===")
# Regular package (calc_pkg has __init__.py)
print("Sum from calc_pkg.ops.add(4, 6):", add(4, 6))

# Namespace package (ns_pkg has NO __init__.py)
print("Namespace package:", ns_pkg.notes.get_note())
print("ns_pkg.__file__:", ns_pkg.__file__)


async def download_file(file_name, seconds):
    print("Downloading:", file_name)
    await asyncio.sleep(seconds)  # Waits without blocking other async tasks
    print("Done:", file_name)


async def main():
    print("\n=== 3.4 Asyncio ===")
    t1 = asyncio.create_task(download_file("notes.pdf", 1))
    t2 = asyncio.create_task(download_file("slides.pptx", 1))
    await t1
    await t2


asyncio.run(main())
