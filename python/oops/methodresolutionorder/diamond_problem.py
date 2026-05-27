class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

def main():
    d = D()
    d.show()
    print(D.mro())

if __name__ == "__main__":
    main()

#   A
#  / \
# B   C
# \   /
#   D

# Python uses C3 Linearization Algorithm to create this order.
#
# This ensures:
#
# No duplicate searching
# Predictable method lookup
# Consistent inheritance behavior