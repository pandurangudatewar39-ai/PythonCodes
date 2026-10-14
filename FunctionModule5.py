from Marvellous import *
def main():
    print("enter first number:")
    Value1=int(input())

    print("enter second number:")
    Value2=int(input())

    Ret=Addition(Value1 , Value2)        

    print("addition is:",Ret)

    Ret=substraction(Value1 , Value2)
    print("substraction is:",Ret)

if __name__=="__main__":
    main()