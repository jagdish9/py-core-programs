def main():
    d1 = {'a': 1}
    d2 = {'b': 2}

    result = {**d1, **d2}
    print(result)

if __name__ == "__main__":
    main()

# Here ** is called the dictionary unpacking operator.
#
# It means:
#
# “Take all key-value pairs from this dictionary and put them here.”