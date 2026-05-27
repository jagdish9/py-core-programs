def main():
    nested = [[1, 2], [3, 4]]

    #Normal way
    flat = []
    for sublist in nested:
        for item in sublist:
            flat.append(item)
    print(flat)

    #Using Comprehension
    flatten = [item for sublist in nested for item in sublist]
    print(flatten)

if __name__ == "__main__":
    main()