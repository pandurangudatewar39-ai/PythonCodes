def main():
    try:
        
        print("Enter first No")
        No1=int(input())
    
        print("Enter second No")
        No2=int(input())

        Ans=No1/No2
        print("Division is succesful")

    except ZeroDivisionError as zobj:
        print("Exception occured due to second operand is zero:",zobj)

    print("Result is:",Ans)

if __name__=="__main__":
    main()