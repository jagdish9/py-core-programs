def main():
    str = "programming"

    vowel_count = 0
    for ch in str.lower():
        if ch in "aeiou":
            vowel_count += 1
    print(vowel_count)

if __name__ == '__main__':
    main()