def main():
    str = "madam"
    print(str)

    if str == str[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

if __name__ == '__main__':
    main()