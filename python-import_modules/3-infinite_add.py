#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num = 0
    x = len(sys.argv)
    for i in range(1, x):
        num += int(sys.argv[i])
    print("{:d}".format(num))
