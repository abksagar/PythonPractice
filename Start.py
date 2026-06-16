print("Jay Ganesh...")

no =11

print("Value of no is :",no)  # 
print("id of no is:",id(no))
print("type of no is:",type(no))


a=10
b=10
print("Value of a is :",a)
print("Value of b is :",b)
print("id of a is:",id(a))
print("id of b is:",id(b))
print("type of a is:",type(a))
print("type of b is:",type(b))

print(id(a)==id(b))

a=[10]
b=[10]
print("Value of a is :",a)
print("Value of b is :",b)
print("id of a is:",id(a))
print("id of b is:",id(b))
print("type of a is:",type(a))
print("type of b is:",type(b))

print(id(a)==id(b))

a=(10,"Jay Ganesh",4.15)
a=[10,"Jay Ganesh",4.15]
print("Value of a is :",a)
print("id of a is:",id(a))  
print("type of a is:",type(a))
a[0]=20   # we cannot change the value of tuple because it is immutable
print(a[0])


x=10
print(hash(x))

s="Jay Ganesh"
print(hash(s))

c=10.9
print(hash(c))

print(hash(x))



