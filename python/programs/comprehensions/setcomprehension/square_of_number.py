def main():
    nums = [1, 2, 2, 3]

    result = {x*x for x in nums}

    print(result)

if __name__ == "__main__":
    main()