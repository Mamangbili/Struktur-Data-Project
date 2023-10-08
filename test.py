class A:
    a : int
    def f(self):
        print('cetak A')

class B(A):
    b : int
    def f(self):
        print('cetak B')

class C(A):
    c : int

class E(C):
    e : int
    # def f(self):
    #     print('cetak E')

class D(E,B):
    d: int
    def f(self):
        print('cetak D')
        super().f()

d = D()
b = B()

print([cls.__name__ for cls in D.__mro__])

    