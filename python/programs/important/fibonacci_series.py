def main():
    n = 10
    a, b = 0, 1

    for _ in range(n):
        print(a, end=" ")
        #a, b = b, a + b
        tmp = a
        a = b
        b = tmp + b

if __name__ == "__main__":
    main()