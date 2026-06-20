import sys
total=0

print("AAA",sys.getsizeof(total))
for i in range(1,11):
    total= total+i
print("Total is :",total)


for i in range(1,4):
    for j in range(1,4):
        print(i,"*",j,"=",i*j)



def multuply(x,y):
    return x*y

print(multuply(10,20))

a=5
print("type of a is:",type(a))

a=5.5
print("type of a is:",type(a))

a="Pyhton"
print("type of a is:",id(a))

a= a+ "3"
print("type of a is:",id(a))


d={1:"one",1:"ONE",2:"TWO"}
print(d)

r= range(5)
print(r)   #range (0,5)
print(list(r)) 



c=100

def globalv():
    global c
    c= c +100
    print("Value of c is :",c+1)

globalv()












































  # It will print the last value of the key because it is overwritten