def Summation(Data):
    sum=0
    
    for no in Data:
        sum=sum+no

    return sum

def main():
    size=0
    Arr=list()
    
    print("Enter the no of elements:")
    size=int(input())

    print("Enter the elements")
    for i in range(size):
        no=int(input())
        Arr.append(no)

    ret=Summation(Arr)
 
    print("Summation is:",ret)

if __name__=="__main__":
    main()