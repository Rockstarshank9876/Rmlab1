a=10
print("methods available on a",dir(a))

a=-10
print("abs of a",a.__abs__())
b=22
print("add",a.__add__(b))

str='hello'
print("methods for atr is",dir(str))

c=22
print("equals",b.__eq__(c))
e=10e4
print(e)
print(type(e))

e=241224123232312312323.5
print(e)

list=[1,2,3]
print(dir(list))