def main():
    s1 = {1, 2}
    s2 = {1, 2, 3, 4}

    print(s1.issubset(s2))
    print(s2.issuperset(s1))

if __name__ == "__main__":
    main()