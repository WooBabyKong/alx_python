import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    num_args = len(argv)

    if num_args == 0:
        arg_str = "."
    elif num_args == 1:
        arg_str = "argument:"
    else:
        arg_str = "arguments:"

    print("Number of argument{} {}".format("s" if num_args != 1 else "", arg_str))
    
    for i, arg in enumerate(argv, start=1):
        print("{}: {}".format(i, arg))