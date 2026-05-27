def main():
    str = "banana"

    #Approach 1
    result = ""
    for ch in str:
        if ch not in result:
            result += ch
    for ch1 in result:
        print(ch1, ":", str.count(ch1))

    frequency = {}

    #Approach 2
    for ch in str:
        frequency[ch] = frequency.get(ch, 0) + 1
    print("frequency:", frequency)

if __name__ == '__main__':
    main()