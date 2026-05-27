def simple_gen():
    yield "First"
    yield "Second"

def main():
    gen = simple_gen()
    for val in gen:
        print(val)

if __name__ == '__main__':
    main()