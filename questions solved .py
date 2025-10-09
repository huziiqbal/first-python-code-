# 1. to check if word is palindrome or not ⚠️ 

word = input ( " enter a word to check if it is a palindrome word ")

reversed_word = word [::-1]



if len(word) <= 0 :
  print("enter the word first")
elif word == reversed_word : 
  print (" yes the word is palindrome ")

else : 
  print ( " no the word is not palindrome ")
 


# 2. finding multiples of any number 

number = int (input( " enter the number you want multiples of ")) 
for e in range (1,11):
  print ( number*e)

# 3. even and odd number finder from list


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 58, 47, 86, 52, 55, 99,85,9,6,88,79,89,58,68,8]
k=[]
g=[]
for w in list:
  h=w%2==0 
  if h:
    k.append(w)
print("even numbers from list are : ")
print(k)
print ("                                                                                                            ") 

for t in list:
  s=t%2 !=2 
  if s:
    g.append(t)
print ( "odd numbers from list are :")
print(g)


# 4. finding repeating entry in a list 

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 58, 47, 86, 52, 55, 99,85,9,6,88,79,89,58,68,8]
for t in list:
  if list.count(t) >1:
    print ("repeated number is ",t)
    list.remove(t)

            # for alphabet

list=["d","s","a","e","y","u","t","o",'i','p','u','y','r']
for t in list:
  if list.count(t) >1:
    print ("repeated alphabet is ",t)
    list.remove(t)




       # 5. sorting in ascending and descending order 
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 58, 47, 86, 52, 55, 99,85,9,6,88,79,89,58,68,8]
list.sort()
print ( list)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 58, 47, 86, 52, 55, 99,85,9,6,88,79,89,58,68,8]
list.sort(reverse=True)
print (list)

# 6. compressing string
# list = ("aaabbcccc")
# for t in list:
#  print(t,list.count(t))



list = ("aaabbcccc")
for t in list:
 print('a',list.count('a'))
 print('b',list.count('b'))
 print('c',list.count('c'))
 break

import time
t = time.strftime('%H:%M:%S') 
hour = int(time.strftime('%H'))
hour = int(input("Enter hour: "))
print(hour)

if(hour>=0 and hour<12):
  print("Good Morning Sir!")
elif(hour>=12 and hour<17):
  print("Good Afternoon Sir!")
elif(hour>=17 and hour<0):
  print("Good Night Sir!")









                        # finding specific tuples fron a list 

list = [ (1,2),(4,8),(5,6),(1,2)]

for t in list :
   if (t[0]+t[1]  >= 10 ):
     print ((t[0],t[1]))




              # reversing a tuple by first converting it into list and then in tuple



# data = ( 1,2,3,4)
# pan = list(data)
# pan.sort( reverse = True)                    #OUTPUT = ( 4,3,2,1,)
# data = tuple ( pan)
# print ( data)


                   # Taking a string from the user and count how many times each word occurs. Store the result in a dictionary.

Input= "python is fun and python is easy"
c = Input.split()

for v in c:
  print(v, ":",Input.count(v))

                # finding the max and min value kye feom a dictionary
marks = {'huzi': 150, 'hong':142, 'hang':80}
r= marks.get(max(marks))
print(r)
for y in marks:
  if marks[y] == r:
    print(y)


                        # try and except simple ques
try:
  l = [1, 5, 6, 7]
  i = int(input("Enter the index: "))
  print(l[i])

except:
    print(l[len(l) - 1])
    print( "the index", {i} ,"is not in the list")
    print("but we have the last element of the list which is", "'",l[len(l) - 1], "'")

finally:
 
    print( "the try and except block is finished")

   #RAISING CUSTOM ERROR 
a = (input("Enter any value between 5 and 9"))

class HuzaifaerError(Exception):
    pass

if a== "quit":
  print( "you choose to quit")

else:
  try:
   num=int(a)
   if(int(a)<5  or int(a)>9 ):
    raise ValueError("Value should be between 5 and 9")
   else: 
     print("you entered ",num)
  except ValueError :
   print("the value should be betweeen 5and 9")


     # finding the nearest square of given input
num  = float(input('Enter a number :'))
g=[]
f=[]
c=[]
for i in range (1,1000):
      k= i**2
      g.append(k)
      if i**2 == num:
       print("the number you entered is a perfect square")
       break

      else :
  
         h= abs(num-k)  
         f.append(h)
         c.append(k)
a=f.index(min(f))
y=c[a]
 
          
        

print(f'the nearest square to your number is {y}')
