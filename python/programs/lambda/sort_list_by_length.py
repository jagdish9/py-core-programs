def main():
    list1 = ["java", "python", "c++", "javascript"]
    print(list1)

    list1.sort()
    print(list1)

    list1.sort(key=lambda s: len(s))

    print(list1)

if __name__ == "__main__":
    main()