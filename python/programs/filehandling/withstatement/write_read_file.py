def main():
    with open("test.txt", "w") as file:
        file.write("file handling with statement")

    with open("test.txt", "r") as file:
        data = file.read()
        print(data)

if __name__ == "__main__":
    main()