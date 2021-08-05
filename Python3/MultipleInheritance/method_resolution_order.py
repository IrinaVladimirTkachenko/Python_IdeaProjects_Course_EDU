# Method Resolution Order (MRO)

#  A
# / \
# B C
# \ /
#  D

class A:
    pass
    #def some_method(self):
     #   print('Method of class A')

class B(A):
    pass
    #def some_method(self):
     #   print('Method of class B')

class C(A):
    pass
    #def some_method(self):
     #   print('Method of class C')

class D(B, C):
    pass
    #def some_method(self):
     #   print('Method of class D')
# __mio__, mro, help()

print(D.__mro__)
print(D.mro())
help(D)


#some_object = D()
#some_object.some_method()

