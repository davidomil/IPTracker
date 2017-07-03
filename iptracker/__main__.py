#!/usr/bin/env python3
import argparse

import sys
import iptracker


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parser = argparse.ArgumentParser(description='Track your IP in realtime')
    # parser.add_argument("--", help="increase output verbosity")

    iptracker.main(parser.parse_args())


if __name__ == "__main__":
    main()
