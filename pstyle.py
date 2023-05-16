#!/usr/bin/python3
# pycodestyle.py
""" pstyle.py - a module that passes the pycodestyle check"""

from datetime import datetime


def time():
    """Simple function to print time"""
    time = datetime.now()
    print(time)


if __name__ == '__main__':
    time()
