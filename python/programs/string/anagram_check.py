def main():
    str1 = "listen"
    str2 = "silent"

    if sorted(str1) == sorted(str2):
        print("Anagram")
    else:
        print("Not Anagram")
        
if __name__ == '__main__':
    main()