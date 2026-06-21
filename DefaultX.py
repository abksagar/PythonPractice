def Area(PI=3.14,radius):  # Not allowed as PI should be last parameter 
    Ans= PI*radius*radius
    return Ans

def main():
    ret = Area(10.5)
    print("Area of circle is:",ret)

    ret = Area(10.5 , 7.12)
    print("Area of circle is:",ret)

    ret = Area(radius=10.5)
    print("Area of circle is:",ret)


if __name__ == "__main__":
    main()
