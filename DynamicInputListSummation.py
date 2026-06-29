def summation(Data):
    sum=0
    for i in Data:
       sum = sum+i

    return sum   

def main():
    Size= 0
    
    print("Enter number of element:")
    Size= int(input())
    Arr = list()
    print("Enter the elements:")
    for i in range(Size):
        no = int(input())
        Arr.append(no)
    
    ret = summation(Arr)
    print("Sum is",ret)
  
      
if __name__ == "__main__":
    main()