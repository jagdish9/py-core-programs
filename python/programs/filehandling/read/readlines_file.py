def main():
    file = open("test.txt", "r")
    list1 = file.readlines()
    print(list1)
    file.close()

if __name__ == "__main__":
    main()

# readlines()
#
# Returns list of lines.