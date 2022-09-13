#!/usr/bin/python

import argparse

# help flag provides flag help
# store_true actions stores argument as True

parser = argparse.ArgumentParser()
   
parser.add_argument('--first name','--Last name', '--age')

args = parser.parse_args()

if args.output:
    print("This is some output")