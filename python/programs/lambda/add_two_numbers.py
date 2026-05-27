def main():
    sum = add(2, 3)
    print(sum)

    #lambda function
    sum2 = lambda a,b : a + b
    result = sum2(2,3)
    print(result)

#Normal function
def add(a, b):
    return a + b

if __name__ == "__main__":
    main()