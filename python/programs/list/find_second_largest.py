def main():
    nums = [10, 20, 4, 45, 99, 99]

    first = second = float('-inf')
    print(first, second)

    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    print(second)

if __name__ == "__main__":
    main()

# Why use float('-inf')
#
# It ensures any number is larger initially.
#
# Example:
#
# 5 > float('-inf')   # True