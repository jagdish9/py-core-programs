def main():
    nums = [1, 2, 3, 4, 5, 6]

    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    print(result)

    result2 = list(filter(lambda num: num % 2 == 0, nums))
    print(result2)

if __name__ == "__main__":
    main()