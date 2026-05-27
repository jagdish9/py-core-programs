count = 0

def main():
    global count
    with open("app.log", "r") as file:
        for line in file:
            if "ERROR" in line:
                count += 1

    print("Total errors: ", count)

if __name__ == "__main__":
    main()