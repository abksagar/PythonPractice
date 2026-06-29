def CheckEven(No):
    if(No %2 ==0):
        print("Even  number")
    else:
        print("Odd number")    
    


def main():
    value= int(input("Enter number"))
    CheckEven(value)

if __name__ == "__main__":
    main()    