import sys
from add_0 import add

def main():
    argv = sys.argv[1:]
    num_args = len(argv)

    print("Number of argument{}: {}:".format('s' if num_args != 1 else '', num_args))

    for i, arg in enumerate(argv, start=1):
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    main()