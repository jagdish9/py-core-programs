class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    pass

class Cat(Animal):
    def sound(self):
        print("Cat sound")

def main():
    d = Dog()
    d.sound()
    c = Cat()
    c.sound()
    a = Animal()
    a.sound()

if __name__ == "__main__":
    main()