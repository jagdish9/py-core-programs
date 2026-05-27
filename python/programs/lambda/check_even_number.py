def main():
    even_number = lambda x : x % 2 == 0
    result = even_number(5)
    print(result)
    result = even_number(6)
    print(result)

if __name__ == '__main__':
    main()