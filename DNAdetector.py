import sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument('s', nargs='?', default=sys.stdin)
args = parser.parse_args()

s = args.s

def validSequence(s):
    valid = 'ACTGU'
    for letter in s:
        if letter not in valid:
            print("false")
    print("true")


validSequence(s)
