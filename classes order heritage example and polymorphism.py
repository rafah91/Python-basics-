#polymorphism:can't inheritate two objects that are doing the same thing between two different classes

class A:
    def do(self):
        print('in A')
class B(A):
    pass
class C:
    def do(self):
        print('in C')
class D(B,C):
    pass

j=D()
j.do()
