#!/usr/bin/python3
"
A Python script that takes in a URL, sends a request to the URL and display
"

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.getheader("X-Request-Id")
        print(header)
