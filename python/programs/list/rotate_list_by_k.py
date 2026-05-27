def main():
    nums = [1, 2, 3, 4, 5]
    k = 2
    k = k % len(nums)

    result = nums[-k:] + nums[:-k]

    print(result)

    k2 = -1
    k2 = k2 % len(nums)

    result2 = nums[-k2:] + nums[0:-k2]
    print(result2)

    k3 = -3
    k3 = k3 % len(nums)

    result3 = nums[-k3:] + nums[:-k3]
    print(result3)

if __name__ == '__main__':
    main()