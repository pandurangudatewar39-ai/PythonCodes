from MarvellousLibrary import filterX, MapX, ReduceX
CheckEven=lambda no: (no%2==0)

increment=lambda no: no+1

Addition=lambda no1,no2: no1+no2



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