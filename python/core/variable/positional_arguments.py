import math

def main():
    sum = add(1, 2, 3)
    print(sum)
    printAll(1,2, 3)

def add(*args):
    return sum(args)

def printAll(*args):
    for arg in args:
        print(arg)

if __name__ == '__main__':
    main()

#
# * → unpack iterable/list/tuple