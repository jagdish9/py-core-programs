def main():
    names = ["java", "python", "golang"]
    result = []
    for name in names:
        result.append(name.upper())
    print(result)

    #comprehension way
    result1 = [name.upper() for name in names]
    print(result1)

if __name__ == "__main__":
    main()