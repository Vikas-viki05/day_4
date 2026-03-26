import os
import socket
import platform
from datetime import datetime

def system_info():
    print("---- SYSTEM INFO ----")

    # Date & Time
    now = datetime.now()
    print("Date & Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

    # Hostname
    hostname = socket.gethostname()
    print("Hostname:", hostname)

    # Python Version
    print("Python Version:", platform.python_version())

    # Current User
    user = os.getenv("USER") or os.getenv("USERNAME")
    print("Current User:", user)

    # Files in Directory
    files = os.listdir(".")
    print("\nFiles in Directory:")
    for f in files:
        print("-", f)

    # File Count
    print("\nTotal Files:", len(files))


def user_input_feature():
    print("\n---- USER INPUT FEATURE ----")
    name = input("Enter your name: ")
    print(f"Hello, {name}! Welcome to DevOps Project 🚀")


if __name__ == "__main__":
    system_info()
    user_input_feature()
