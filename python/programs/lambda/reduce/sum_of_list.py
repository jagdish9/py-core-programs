from functools import reduce

def main():
    nums = [1, 2, 3, 4]
    result = reduce(lambda a, b: a + b, nums)
    print(result)

if __name__ == "__main__":
    main()