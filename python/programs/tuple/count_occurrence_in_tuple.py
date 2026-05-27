def main():
    t = (1, 2, 2, 3, 2)

    frequency = {}

    for num in t:
        frequency[num] = frequency.get(num, 0) + 1

    print(frequency)

if __name__ == '__main__':
    main()