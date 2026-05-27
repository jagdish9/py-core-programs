def numbers():
    yield 1
    yield 2
    yield 3

def main():
    gen = numbers()
    print(gen)
    print(next(gen))
    print(next(gen))

if __name__ == '__main__':
    main()

# Benefit:
#   memory efficient