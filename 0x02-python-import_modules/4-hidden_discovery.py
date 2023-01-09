#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    hidden_name = dir(hidden_4)

    for name in hidden_name:
        if not name.startswith("__"):
            print(name)
