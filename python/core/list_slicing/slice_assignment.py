def main():
    nums = [1, 2, 3, 4]

    print(nums)

    nums[1:3] = [20, 30] # Replace elements

    print(nums)

    nums[1:3] = [] # Remove elements

    print(nums)

if __name__ == '__main__':
    main()