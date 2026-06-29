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