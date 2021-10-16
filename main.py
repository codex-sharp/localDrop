import os
import argparse
from utils import *

# SYSTEM IP ADDRESS
IP_ADDRESS = '0.0.0.0'

parser = argparse.ArgumentParser()
parser.add_argument('--a', help='Action to perform')
parser.add_argument('--f', help='File to share')
args = parser.parse_args()

def main():
    action = args.a
    file = args.f
    # actions here
    if action == 'share':
        generate_share_link(file, IP_ADDRESS)
    elif action == 'list_shares':
        list_files_shared()
    elif action == 'delete_share':
        delete_shared_file(file)
    # elif action == 'start_server':
    #     # todo

main()