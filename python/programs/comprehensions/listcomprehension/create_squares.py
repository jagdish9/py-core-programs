def main():
    nums = [1, 2, 3, 4]
    result = []

    for num in nums:
        result.append(num*num)
    print(result)

    #comprehension way
    result1 = [num*num for num in nums]
    print(result1)

if __name__ == "__main__":
    main()