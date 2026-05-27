def main():
    nums = [1, 2, 3, 4, 5, 6]
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    print(result)

    #comprehension way
    result1 = [num for num in nums if num % 2 == 0]
    #result2 = [num % 2 == 0 for num in nums]
    print(result1)
    #print(result2)

if __name__ == "__main__":
    main()