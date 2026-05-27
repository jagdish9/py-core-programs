def main():
    d = {'a': 1, 'b': 2, 'c': 3}
    result = {}

    for key, value in d.items():
        result[value] = key

    print(result)

if __name__ == '__main__':
    main()