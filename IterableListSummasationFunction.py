def summation(Data): 
    ans=0

    for no in Data:
        ans= ans+no

    return ans     
        

def main():
    Marks =[78,90,56,95,77] 
    ret = summation(Marks)
    print("Addition is: ",ret)


if __name__ == "__main__" :
    main()

    

