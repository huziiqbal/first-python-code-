#Date = 2-11-2025
binary_number =input("Enter the binary number you want ones complement of :")
g=[]
for y in binary_number:
    if y == '0':
        g.append('1')
    elif y == '1':
        g.append('0')
print(f'ones complement of {binary_number} is : {"".join(g)}')
