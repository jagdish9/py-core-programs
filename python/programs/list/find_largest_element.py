def main():
    nums = [4, 7, 1, 9, 2]
    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num

    print(largest)

if __name__ == '__main__':
    main()