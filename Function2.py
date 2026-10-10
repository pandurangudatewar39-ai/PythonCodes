def Addtion(No1,No2):
    Ans=0
    Ans=No1+No2
    return Ans

def main():
    print("enter first number:")
    Value1=int(input())

    print("enter second number:")
    Value2=int(input())
    print("enter second number:")
    Value3=int(input())
    
    Ret=Addtion(Value1 , Value2, Value3)  

    print("addition is:",Ret)

if __name__=="__main__":
    main()