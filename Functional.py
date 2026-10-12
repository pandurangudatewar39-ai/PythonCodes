Addition=lambda no1,no2: no1+no2
    
Substraction=lambda no1,no2: no1-no2
   
print("Enter first no:")
Value1=int(input())

print("Enter second no:")
Value2=int(input())

ret=Addition(Value1,Value2)
print("Addition is:",ret)

ret=Substraction(Value1,Value2)
print("Substraction is:",ret)