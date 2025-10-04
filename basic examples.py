      # basic try , except and finally example
try:
  
  i = int(input("Enter the first number "))
  j = int(input("Enter the second number "))
  o=(int(i)*int(j))
  print(o)

except ValueError:
  print("you didn't entered valid numbers")
  
finally:
 print("the program has ended")

 # comparing numbers using short hand if else statements 
a = int(input("enter the first number"))
b = int(input("enter the second number"))
c = int(input("enter the third number"))
print("the largest number anongg all the input is :")
print(a) if a > b >c or a>c>b else print(b) if b>a>c or b>c>a else print(c)
