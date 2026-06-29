from functools import reduce

def CheckEven(No):
    return (No % 2 ==0)

def increment(No):
    return No+1

def Addition(No1,No2):
    return No1+No2

#filer --> will take 1 paramet and return boolean 
#map --> will take 1 parameter and return parameter not boolean 
#reduce --> will always accept 2 parameter and return 1 value.

def main():
    Data = [13,12,8,10,11,20]

    print("Input data is",Data)

    FData = list(filter(CheckEven, Data))
    print("Data after filer :",FData)

    MData= list(map(increment,FData))
    print("Data of map",MData)

    rData= reduce(Addition,MData)
    print("reduce data",rData)

if __name__ == "__main__" : 
    main()