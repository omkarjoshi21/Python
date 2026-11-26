# Simple user-defined module used in modules_packages_asyncio.py

APP_NAME = "IMCC Study App"
VERSION = "1.0"


def greet(name):
    print("Hello", name + "! Welcome to", APP_NAME, "v" + VERSION)
