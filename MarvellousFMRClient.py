from MarvellousLibrary import filterX,mapX,reduceX

CheckEven = lambda  No:(No % 2 ==0)

increment= lambda No:( No+1)

Addition = lambda No1, No2 : No1+No2

def main():
    Data = [13,12,8,10,11,20]

    print("Input data is",Data)

    FData = list(filterX(CheckEven, Data))
    print("Data after filer :",FData)

    MData= list(mapX(increment,FData))
    print("Data of map",MData)

    rData= reduceX(Addition,MData)
    print("reduce data",rData)

if __name__ == "__main__" : 
    main()