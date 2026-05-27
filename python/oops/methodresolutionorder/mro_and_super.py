class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

def main():
    b = B()
    b.show()

if __name__ == "__main__":
    main()

# super() checks the next class in MRO.