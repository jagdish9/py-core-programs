def main():
    try:
        x = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("finally, always executes")

if __name__ == '__main__':
    main()