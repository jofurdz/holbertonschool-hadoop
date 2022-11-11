#!/usr/bin/env python3
"""contains function download()"""

from snakebite.client import Client


def download(l):
    """retrieves from the HDFS files listed in l
    and store them in the home /tmp folder of the user
    """
    client = Client('127.0.1.1', 9000)

    for x in client.copyToLocal(l, '/tmp'):
        print(x)
