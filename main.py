#!/usr/bin/env python3
import argparse

from iptracker.iptracker import main

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Track your IP in realtime')
    # parser.add_argument("--", help="increase output verbosity")

    args = parser.parse_args()
    main(args)
