def main():
    text = "python is easy and python is powerful"

    frequency = {}

    for word in text.split():
        frequency[word] = frequency.get(word, 0) + 1

    print(frequency)

if __name__ == '__main__':
    main()