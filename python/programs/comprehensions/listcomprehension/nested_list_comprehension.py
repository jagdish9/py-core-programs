def main():
    matrix = [[0 for j in range(3)] for i in range(2)]
    print(matrix)

    matrix1 = []
    for i in matrix:
        row = []
        for j in i:
            row.append(j)
        matrix1.append(row)
    print(matrix1)

if __name__ == "__main__":
    main()