def main():
    file = open("test.txt", "r")
    data = file.read()
    print(data)
    file.close()

if __name__ == "__main__":
    main()

# read()
#
# Reads entire file.