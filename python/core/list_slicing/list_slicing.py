def main():
    nums = [10, 20, 30, 40, 50]
    print(nums)

    print(nums[1:4]) # start and end

    print(nums[:3]) # First 3 elements

    print(nums[2:]) # Get elements from index onward

    nums_copy = nums[:]
    print(nums_copy)

    print(nums[-1:]) # last elements

    print(nums[::-1]) # reverse a list

    print(nums[::2]) # skip elements using step

    print(nums[-4:-1]) # negative indexing

if __name__ == '__main__':
    main()

# list[start:end:step]
# start → index where slicing begins (inclusive)
# end → index where slicing stops (exclusive)
# step → how many positions to move

# Negative indexes count from the end:
#
# -1 -> last element
# -2 -> second last