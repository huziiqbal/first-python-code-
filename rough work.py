n = int(input ("enter the number of lines of your inverted pyramid "))
o=[]
k=(n*2)-1
for i in range(1,k):
 o.append(k)
h=len(o)

u=0
while u<h:
  o[u]="*"
  u=u+1


for t in o :
 
  o[0]=" "
  o[h-1]=" "

  for r in o :

   print(t,r)
  break