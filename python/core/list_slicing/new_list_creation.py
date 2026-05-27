def main():
    list1 = [1, 2, 3]
    list2 = list1[:] # create copy

    print(list1 is list2)

    print(list1)
    print(list2)

if __name__ == '__main__':
    main()

# Both lists contain same values but are different objects.