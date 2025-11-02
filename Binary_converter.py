decimal_number = int(input("Enter the decimal number you want to convert to binary:"))
p=[]
p.append(decimal_number%2)
k=decimal_number//2
while k>0:
    p.append(k%2)
    k=k//2
w= p[::-1]
g= "".join(str(i) for i in w)
print(f'The binary form of {decimal_number} is {g}')
