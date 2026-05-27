class Dog:
    def speak(self):
        return "Woof"

def new_speak(self):
    return "Meow (patched!)"

def main():
    # Monkey patching
    Dog.speak = new_speak

    d = Dog()
    print(d.speak()) # Output: Meow (patched!)

if __name__ == "__main__":
    main()