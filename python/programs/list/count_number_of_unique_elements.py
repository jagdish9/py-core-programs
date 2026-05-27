def main():
    chars = ['a','b','h','f','a','b','f','f','f']

    frequency = {}

    for char in chars:
        frequency[char] = frequency.get(char, 0) + 1
    print(frequency)

if __name__ == "__main__":
    main()