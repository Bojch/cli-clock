import argparse

def parser():
    ap = argparse.ArgumentParser(prog='./clock')
    ap.add_argument('app', choices=['alarm', 'timer'])
    ap.add_argument('-t', '--time', help='Format: Y-m-d h:i [2016-07-22 12:33]')
    ap.add_argument('-s', '--sec')
    ap.add_argument('-m', '--msg', help='The message you want to get from notification.')
    return ap.parse_args()
