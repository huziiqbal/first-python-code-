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