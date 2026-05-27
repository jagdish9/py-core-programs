def main():
    file = open("test.txt", "r")
    print(file.readline())
    print(file.readline())
    file.close()

if __name__ == "__main__":
    main()

# readline()
# Reads one line at a time.