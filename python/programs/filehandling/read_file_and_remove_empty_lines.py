def main():
    with open("test2.txt", "r") as file:
        data = file.read()
    print(data)

    with open("test2.txt", "r") as file1:
        lines = [line.strip() for line in file1 if line.strip()]
    print(lines)

if __name__ == "__main__":
    main()