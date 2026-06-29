def CheckEven(No):
    # if(No %2 ==0):
    #     return True
    # else:
    #    return False  

    return (No%2 == 0)
    


def main():
    value= int(input("Enter number"))
    ret = CheckEven(value)
    if(ret == True):
        print("its a even number")
    else:
        print("Its odd number")    

if __name__ == "__main__":
    main()    