
CheckEven = lambda  No:(No % 2 ==0)

increment= lambda No:( No+1)

Addition = lambda No1, No2 : No1+No2


def filterX(Task,Elements):
    Result =[]

    for no in Elements:
        ret = Task(no)     # this calls checkEven(no)

        if(ret == True):
            Result.append(no)

    return Result

def mapX(Task,Elements):
    Result=[]

    for no in Elements:
        ret = Task(no)   #this calls to increment
        Result.append(ret)

    return Result

def reduceX(Task, Element):
    sum = 0

    for no in Element:
        sum = Task(sum,no)

    return sum

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