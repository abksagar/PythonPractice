from functools import reduce

CheckEven = lambda  No:(No % 2 ==0)

increment= lambda No:( No+1)

Addition = lambda No1, No2 : No1+No2


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