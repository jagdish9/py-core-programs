def main():
    names = ["java", "python", "javascript", "golang"]

    result = []
    result1 = []
    for name in names:
        result.append(name.upper())
        result1.append(name.capitalize())
    print(result)
    print(result1)

    # lambda expression
    result2 = list(map(lambda s: s.upper(), names))
    print("lambda expression:\n", result2)

if __name__ == "__main__":
    main()