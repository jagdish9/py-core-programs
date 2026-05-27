def main():
    str1 = "aaabbc"

    length = len(str1)
    count = 1
    result = ""

    for i in range(length-1):
        if str1[i] == str1[i+1]:
            count = count + 1
        else:
            result = result + str1[i] + str(count)
            count = 1
    result = result + str1[-1] + str(count)

    print(result)

if __name__ == '__main__':
    main()