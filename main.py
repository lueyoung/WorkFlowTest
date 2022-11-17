#!/usr/bin/env python

import os

if __name__ == "__main__":
    x = os.environ["XXX"]
    print(x)
    if (len(x) == 0): 
        print("null")
    else:
        print("123")
