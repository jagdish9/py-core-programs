def main():
    with open("test.txt", "r") as file:
        data = file.read()

    words = data.split()

    print("Word count: ", len(words))

if __name__ == "__main__":
    main()