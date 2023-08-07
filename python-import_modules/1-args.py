import sys

def main():
    argv = sys.argv[1:]
    num_args = len(argv)

    print(f"Number of argument{'s' if num_args != 1 else ''}: {num_args}{'.' if num_args == 0 else ':'}")

    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    main()