def main():
    str = "Hello World"

    reverse = str[::-1]

    print(str)
    print(reverse)

    rev = ""
    for ch in str:
        rev += ch
    print(rev)

    rev1 = ""
    for ch in str:
        rev1 = ch + rev1
    print(rev1)

if __name__ == '__main__':
    main()