def main():
    dictionary = {'a': 10, 'b': 50, 'c': 20}

    max_key = max(dictionary, key=dictionary.get)

    print(max_key)

if __name__ == "__main__":
    main()