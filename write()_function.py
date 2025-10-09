# #writelines() function

h=['"he is a good boy"','"he is also very hardworking"','"but sometimes he gets tired"']
k= open("sample.py","w") 

for u in h:
   k.write(u+'\n')
k.close()

# readlines function
y= open("sample.py","r")
while True:
   g=y.readline()
   if not g:
     break
   print(g,end="")
y.close()
  


w= open("sample.py","r")
f=w.readline()
print(f,end="")
w.close()

