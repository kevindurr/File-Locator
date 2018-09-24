#!/bin/python2.7
import os, sys
from stat import*
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('root', help="root Parameter")
parser.add_argument('-name', help="Name Parameter")
parser.add_argument('-grep', help="grep Parameter")
args = parser.parse_args()
    
def walktree(top):
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname).st_mode
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walktree(pathname)
        elif S_ISREG(mode):
            # It's a regular file, let's calculate the line number and pathname
            number = 0 
            if S_ISREG(mode):
                if not args.name or re.match(args.name + "$", f):
                    if not args.grep:
                        print pathname
                    else:
                        for line in open(pathname):
                            number += 1
                            if re.search(args.grep, line):
                                print pathname, number,":", line,
if __name__ == '__main__':
    walktree(args.root)
