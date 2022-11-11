#!/usr/env/env python3
"""contains function createdir()"""

from snakebite.client import Client


def createdir(l):
    """Creates a directory from the path"""
    client = Client('127.0.1.1', 9000)

    for path in client.mkdir(l, create_parent=True):
        print(path)
