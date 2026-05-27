def main():
    str = "programming_p"
    print(str)

    for ch in str:
        if str.count(ch) == 1:
            print(ch)
            break

if __name__ == '__main__':
    main()