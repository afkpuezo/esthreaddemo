"""
Contains a function to print all of the numbers in a given range, with a delay between
each print.

@author: Andrew Curry
"""
import time
import sys
from threading import Lock


def print_range(start: int, end: int, delay: float, lock : Lock):
    """
    Contains a function to print all of the numbers in a given range, with a delay between
    each print.
    start and end params are inclusive.
    delay should be measured in seconds.
    Assumes end > start.
    Intended for use in threads created by main.py
    """
    for x in range(start, end + 1):
        time.sleep(delay)
        lock.acquire()
        print(str(x))
        lock.release()