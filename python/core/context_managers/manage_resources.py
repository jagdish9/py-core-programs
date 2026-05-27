def main():
    with open("xyz_abc.txt", "w") as file:
        file.write("Hello World!")

if __name__ == '__main__':
    main()

# Automatically closes file.
#
# Equivalent to:
#
# try
# finally