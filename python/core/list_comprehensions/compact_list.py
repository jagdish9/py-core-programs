def main():
    #square
    squares = [x*x for x in range(5)]
    print(squares)

    #even numbers
    even = [x for x in range(10) if x % 2 == 0]
    print(even)

if __name__ == '__main__':
    main()