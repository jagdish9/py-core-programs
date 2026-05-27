import copy

if __name__ == "__main__":
    numbers = [[1, 2], [3, 4]]

    print(numbers)

    second_numbers = copy.copy(numbers)

    second_numbers[0][0] = 200

    print("first:", numbers)
    print("second", second_numbers)