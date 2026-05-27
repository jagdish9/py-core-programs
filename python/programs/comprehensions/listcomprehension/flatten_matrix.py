def main():
    matrix = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    result = []
    for submatrix in matrix:
        for item in submatrix:
            result.append(item)
    print(result)

    #comprehension way
    result1 = [item for submatrix in matrix for item in submatrix]
    print(result1)

if __name__ == "__main__":
    main()