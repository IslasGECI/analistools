#!/usr/bin/env python

import argparse

def path_files():
    parser = argparse.ArgumentParser(description='CLI for input and outputs files')
    parser.add_argument('-i', '--input', action='append', nargs='+',help='Input files path')
    parser.add_argument('-o', '--output', action='append', nargs='+', help='Output files path')
    parser.add_argument('-d', '--drop', action='append', nargs='+', help='Drop values')
    return parser.parse_args()