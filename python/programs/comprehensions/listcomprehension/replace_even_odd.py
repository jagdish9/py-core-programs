def main():
    nums = [1, 2, 3, 4]
    result = ["Even" if num % 2 == 0 else "Odd" for num in nums]
    print(result)

if __name__ == "__main__":
    main()