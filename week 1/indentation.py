#purposely raise an indentation error and correct indentation
a=float(input("enter the value of a: "))
b=float(input("enter the value of b: "))
if a<=b:
  print("a is big") 
else:
  print("b is big")

#correct code 
a=float(input("enter the value of a: "))
b=float(input("enter the value of b: "))
if a<=b:
    print("a is small") 
else: 
    print("b is big")