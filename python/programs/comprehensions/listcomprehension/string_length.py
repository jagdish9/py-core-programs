def main():
    words = ["cat", "elephant", "tiger"]
    result = []
    for word in words:
        result.append(len(word))
    print(result)

    #comprehension way
    result1 = [len(word) for word in words]
    print(result1)

if __name__ == "__main__":
    main()