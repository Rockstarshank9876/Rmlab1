a=10
b='10'
c=30
list=[10,20,30,40]
dict1={1:10,2:20,3:30,4:40}
dict2={1:10,2:20,3:30,4:40}
print(id(a),id(b),id(c),id(list),id(list[0]),id(dict[1]))

print(dict1 is dict2)