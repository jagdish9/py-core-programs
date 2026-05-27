def main():
    with open("test.txt", "r") as file:
        lines = file.readlines()

    print("Word count: ", len(lines))

if __name__ == "__main__":
    main()