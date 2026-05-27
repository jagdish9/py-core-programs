def main():
    user(name="Bahadur", age=25, department="Sales")

def user(**kwargs):
    print(kwargs)

if __name__ == '__main__':
    main()

#
# ** → unpack dictionary