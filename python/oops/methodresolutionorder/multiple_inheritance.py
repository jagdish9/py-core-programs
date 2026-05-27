class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    pass

def main():
    c = C()
    c.show()
    #print(C.__mro__)
    #print(C.mro())

if __name__ == "__main__":
    main()

# Output:
#
# A
#
# Why?
#
# Because MRO for C is:
#
# C → A → B
#
# Python checks:
#
# C
# A
# B
#
# It finds show() in A first.