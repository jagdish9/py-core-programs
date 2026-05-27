class A:
    def show(self):
        print("A")

class B(A):
    pass

def main():
    b = B()
    b.show()

if __name__ == "__main__":
    main()

# Python searches like this:
#
# B → A
#
# Since B does not have show(), it checks A.