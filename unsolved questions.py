# replace keys from values in dictionary , keys turn into values and values into keys 
#when 2 keys have same value this is eliminating one , so ,make a default solution to identify if there 
#are same repeating values and if so then solve them by (.setdefault (kkey,[]),append ())  

info = {'Karan':14, 'age':14, 'eligible':21}
k= info.values()
j=info.keys()
r={}
for y in k :
    if y >= 18:
     p = r.setdefault(k,[])
     p.append(j)


     print(r,dict(zip(k,j)) ) # unsolved 
     

     # samjh jaa khud 
a = (input("Enter any value between 5 and 9"))

class HuzaifaerError(Exception):
    pass

