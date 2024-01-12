#!/usr/bin/python3
"""
A Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(email).encode("utf-8")
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
