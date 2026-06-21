# Accept : Multiple parameters
# Return : Multiple Value 

def Marvellous(value1,value2):
    print("Inside Marvellous:",value1,value2)
    return 21,34   # return 21 as a random number to show it return 

def main():
    ret1, ret2 = Marvellous(10,20)
    print("Return values are:",ret1,ret2)

if __name__ =="__main__":
    main()