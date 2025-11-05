#Date = 3-11-2025
conversion_type = input("which type of conversion you want to do?\n 1. for decimal to binary \n 2. for binary to one's complement \n 3. for binary to two's complement\n Enter your choice (1/2/3) :")
if conversion_type == '1':
 p=[]
 decimal_number = int(input("Enter the decimal number you want to convert to binary:"))
 p.append(decimal_number%2)
 k=decimal_number//2
 while k>0:
    p.append(k%2)
    k=k//2
 w= p[::-1]
 g= "".join(str(i) for i in w)
 print(f'The binary form of {decimal_number} is {g}')
if conversion_type == '2':
 g=[]
 binary_number =input("Enter the binary number you want ones complement of :")
 for y in binary_number:
    if y == '0':
        g.append('1')
    elif y == '1':
        g.append('0')
 print(f'ones complement of {binary_number} is : {"".join(g)}')
if conversion_type == '3':
 c,s,k=[],[],[]
 binary_number2 =input("Enter the binary number you want two's complement of :")
 for y in binary_number2:
    if y == '0':
        c.append('1')
    elif y == '1':
       c.append('0')
 f= len(c)
 h = c[::-1]
 for u in h:
    if u == '1':
        k.append('0')
    elif u == '0' :
        k.append('1')
        break
 p = f-(len(k)) -1
 i = 0
 for i in range (p+1):
        s.append(c[i])
        i= i+1
 v = "" . join(s)
 w ="" .join(k[::-1])
 print(f"The Two's complement of {binary_number2}  is : {v+w}")

