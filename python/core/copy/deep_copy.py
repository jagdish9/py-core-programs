import copy

if __name__ == '__main__':
    numbers = [[1, 2], [3, 4]]

    second_numbers = copy.deepcopy(numbers)

    second_numbers[0][1] = 10

    print("first", numbers)
    print("second", second_numbers)