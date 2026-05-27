def main():
    with open("src.txt", "r") as src:
        content = src.read()
        print("read succeed")

    with open("dest.txt", "w") as dest:
        dest.write(content)
        print("write succeed")

if __name__ == "__main__":
    main()