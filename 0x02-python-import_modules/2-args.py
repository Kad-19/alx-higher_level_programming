#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv)
    if (len(argv) == 1):
        print("0 arguments.")
    else:
        if (len(argv) == 2):
            print("1 argument:")
        else:
            print("{} arguments:".format(len(argv) - 1))
        for n in range(1, argc):
            print("{}: {}".format(n, argv[n]))
