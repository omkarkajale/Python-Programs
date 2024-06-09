class A:
    varA='Welcome this A'
class B:
    varB='Welcome this B'
class C(A,B):
    varC='Welcome this C'
D=C()
print(C.varA,C.varB,C.varC)