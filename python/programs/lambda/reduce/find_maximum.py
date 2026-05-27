from functools import reduce

def main():
    nums = [10, 50, 20, 80, 30]

    result = reduce(lambda a, b: a if a > b else b, nums)

    print(result)

if __name__ == "__main__":
    main()