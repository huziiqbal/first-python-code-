# Logic: First take the 1's complement by flipping all bits,
# then manually add 1 by flipping bits from the right until the first 0 is found,
# to get the final 2's complement.
binary_number =input("Enter the binary number you want two's complement of :")
g=[]
for y in binary_number:
    if y == '0':
        g.append('1')
    elif y == '1':
       g.append('0')
s=[]
k=[]
h = g[::-1]
for u in h:
    if u == '1':
        k.append('0')
    elif u == '0' :
        k.append('1')
        break
p = len(g)-(len(k)) -1
i = 0
for i in range (p+1):
        s.append(g[i])
        i= i+1
v = "" . join(s)
w ="" .join(k[::-1])
print(f"The Two's complement of {binary_number}  is : {v+w}")
