def BigBazar():
    print("Inside BB")

    def Amul():
        print("Inside Amul Icecream")



def main():
    BigBazar()
    #Amul()           #error as its not allowed 
    #BigBazar.Amul()    # error not allowed
    
  

if __name__ =="__main__":
    main()