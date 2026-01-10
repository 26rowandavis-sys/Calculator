print("basic calculator ")
print ("Operations - + * / % ")
num1 = float (str(input("enter first number ")))
op = str(input("enter operator(- + * / % ):"))
num2 = float (str(input("enter second number ")))
if op == "+":
    print (num1 + num2)
elif  op == "-":
    print (num1 - num2) 
elif op == "*":
    print (num1 * num2) 
elif op == "/":
    if num2 == "0":
        print ("ZeroDivisionError")
    else:
        print (num1 / num2)      
elif op == "%":
    print (num1 % num2)
else: print ("unknown operator ")    



