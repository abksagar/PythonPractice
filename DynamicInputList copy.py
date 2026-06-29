def main():
    Size= 0
    
    print("Enter number of element:")
    Size= int(input())
    Arr = list()
    print("Enter the elements:")
    for i in range(Size):
        no = int(input())
        Arr.append(no)
    print(Arr)    
        
    

if __name__ == "__main__":
    main()