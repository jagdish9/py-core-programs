def main():
    list1 = ["Apple", "Banana", "Cherry", "Avocado", "Lichi"]
    print(list1)

    result = list(filter(lambda s: s.startswith("A"), list1))
    print(result)

if __name__ == '__main__':
    main()