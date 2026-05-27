def main():
    str = "programming"
    print(str)
    result = ""

    for ch in str:
        if ch not in result:
            result += ch
    print(result)

if __name__ == "__main__":
    main()