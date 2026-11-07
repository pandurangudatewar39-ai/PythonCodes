
CheckEven=lambda no: (no%2==0)

increment=lambda no: no+1

Addition=lambda no1,no2: no1+no2

def filterX(Task,Elements):
    Result=[]
    
    for no in Elements:
        ret=Task(no)     #CheckEven(no)

        if(ret==True):
            Result.append(no)
    
    return Result

def MapX(Task,Elements):
    Result=[]

    for no in Elements:
        ret=Task(no)        #Increment(no)
        Result.append(ret)

    return Result

def ReduceX(Task,Elements):
    sum=0

    for no in Elements:
        sum=Task(sum,no)

    return sum

def main():
    Data=[13,12,8,10,11,20] 

    print("input data is :",Data)

    FData=list(filterX(CheckEven,Data))
    print("data after filter",FData)

    MData=list(MapX(increment,FData))
    print("data after map",MData)

    RData=ReduceX(Addition,MData)
    print("data after reduce",RData)

    
if __name__=="__main__":
    main()