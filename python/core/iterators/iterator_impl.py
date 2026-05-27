def main():
    arr = [1, 2, 3]

    it = iter(arr)

    print(next(it))
    print(next(it))
    print(next(it))

if __name__ == '__main__':
    main()

# Object implementing:
#
# __iter__()
# __next__()