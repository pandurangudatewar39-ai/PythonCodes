CheckEven=lambda no:(no % 2 == 0)

def main():
    Value=int(input("Enter Number : "))

    ret=CheckEven(Value)  #ret=(Value % 2 == 0)

    if (ret==True):
        print("its even number")
    else:
        print("its odd number")

if __name__=="__main__":
    main()