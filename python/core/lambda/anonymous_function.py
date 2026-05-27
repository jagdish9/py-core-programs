def main():
    square = lambda y: y * y
    print(square(7))

    plus = lambda x, y: x + y
    print(plus(3, 4))

    power_of_n = lambda n: n ** 2
    print(power_of_n(3))

    n_power_of_number2 = lambda n: 2 ** n
    print(n_power_of_number2(3))

    add_numbers = lambda n1, n2, n3, n4, n5: n1 + n2 + n3 + n4 + n5
    print(add_numbers(1, 3, 5, 6, 7))

if __name__ == '__main__':
    main()