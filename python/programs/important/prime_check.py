def main():
    n = 29
    is_prime = True

    # O(square root of n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    print(is_prime)

    # O(n)
    is_prim2 = True
    for i in range(2, n):
        if n % i == 0:
            is_prim2 = False
            break

    print(is_prim2)

if __name__ == "__main__":
    main()