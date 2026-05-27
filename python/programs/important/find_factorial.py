def main():
    n = 5

    factorial = 1

    for i in range(1, n+1):
        factorial *= i

    print(factorial)

if __name__ == "__main__":
    main()