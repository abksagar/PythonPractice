no= 11    #Global Variable

def Display():
    a=10                #Local variable
    print(" From Display:",no)
    print("From Display value of a",a)

def Demo():
    print("From Demo:",no)
    print("From Demo a is ",a)

Display()
Demo()