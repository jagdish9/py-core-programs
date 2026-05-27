def main():
    nums = [0, 1, 0, 3, 12]

    result = []

    for num in nums:
        if num != 0:
            result.append(num)

    zeros = [0] * (len(nums) - len(result))

    print(result + zeros)

if __name__ == "__main__":
    main()