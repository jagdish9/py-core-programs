def main():
    nums = [1, 2, 3, 5]

    n = 5;

    expected = n * (n+1) // 2
    actual = sum(nums)

    missing = expected - actual
    print(missing)

if __name__ == "__main__":
    main()