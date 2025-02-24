#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stderr.write("[ERROR] provide correct number of arguments\n")
        sys.exit(1)
    print("GOT CMD:", sys.argv)
