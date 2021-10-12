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
        fid = generate_fid(file)
        share_link = 'http://' + IP_ADDRESS + '?fid=' + fid
        print('File share link:\n {}'.format(share_link))
    elif action == 'start_server':
        # todo
    elif action == 'list_shares':
        # todo
    elif action == 'delete_share':
        # todo

main()
