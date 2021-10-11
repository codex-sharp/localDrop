import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--a', help='Action to perform')
parser.add_argument('--f', help='File to share')
args = parser.parse_args()

def main():
    action = args.a
    file = args.f
    # actions here

main()
