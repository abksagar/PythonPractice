def Addition(val1 , val2):
    Ans = val1 +val2
    return Ans

def main():
   print("Enter first number")
   value1= int(input())
   print("Enter second number")
   value2= int (input())
   ret = Addition (value1, value2)
   print("addition is :", ret)

if __name__ == "__main__" :
    main()
