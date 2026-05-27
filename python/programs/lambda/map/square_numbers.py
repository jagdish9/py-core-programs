def main():
    result = square_number()
    print(result)

    result = square_number_with_map()
    print(result)

#Without map
def square_number():
    nums = [1, 2, 3, 4]

    result = []

    for num in nums:
        result.append(num * num)
    return result

#With map
def square_number_with_map():
    nums = [1, 2, 3, 4]

    return list(map(lambda x: x*x, nums))

if __name__ == "__main__":
    main()