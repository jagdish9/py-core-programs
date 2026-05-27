def main():
    result = []
    for x in range(5):
        result.append(x)
    print(result)

    #instead of above, we can write using comprehension
    result1 = [x for x in range(5)]
    print(result1)

if __name__ == "__main__":
    main()