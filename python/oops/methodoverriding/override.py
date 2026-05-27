class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")

def main():
    c = Child()
    c.show()
    p = Parent()
    p.show()

if __name__ == "__main__":
    main()