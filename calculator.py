value1=int(input("enter the first number:\n"))
operator=input("enter the operator:\n")
value2=int(input("enter the second operator:\n"))
if operator=="+":
    print(value1+value2)
elif operator=="-":
    print(value1-value2)
elif operator=="*":
    print(value1*value2)
elif operator=="/":
    print(value1/value2)
elif operator=="%":
    print(value1%value2)
else:
    print("please enter a valid operator like +, -, *, / or % for calculation")

