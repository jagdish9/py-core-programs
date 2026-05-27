from functools import reduce

def main():
    nums = [1, 2, 3, 4, 5, 6]

    #Step 1: filter even
    even = filter(lambda num: num % 2 == 0, nums)

    #Step 2: square them
    squared = map(lambda num: num*num, even)

    #Step 3: sum all
    result = reduce(lambda num1, num2: num1+num2, squared)
    print(result)



if __name__ == "__main__":
    main()