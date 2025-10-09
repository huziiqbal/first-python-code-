#writelines() function
h = ['"he is a good boy"\n', '"he is very hardworking"\n', '"but sometimes he gets tired"\n']
k = open("sample.py", "w") 
k.writelines(h)
k.close()

# writelines() function
h = ['"he is a good boy"','"he is very hardworking"', '"but sometimes he gets tired"']
k = open("sample.py", "w") 
for u in h:
   k.writelines(u+'\n')
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
