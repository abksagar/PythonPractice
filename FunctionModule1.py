import Marvellousq


def main():
   print("Enter first number")
   value1= int(input())
   print("Enter second number")
   value2= int (input())
   ret = Marvellousq.Addition(value1, value2)
   print("addition is :", ret)

if __name__ == "__main__" :
    main()