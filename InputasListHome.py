def summation(Data):
    sum = 0
    for i in Data:
        sum= sum+i
    return sum    

def main():
    userInput =0
    ArrList= list()
    userInput= int(input("Enter how many numbers to add"))

    for i in range(userInput):
        no= int(input("Enter number in list"))
        ArrList.append(no)
    
    ret= summation(ArrList)
    print("sum is", ret)






if __name__ == "__main__":
    main()