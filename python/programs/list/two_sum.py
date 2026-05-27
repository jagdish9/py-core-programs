def main():
    nums = [2, 11, 7, 15]
    target = 9

    seen = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in seen:
            print(seen[diff], i)
            break

        seen[num] = i

if __name__ == "__main__":
    main()