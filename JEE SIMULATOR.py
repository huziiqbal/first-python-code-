print ("WELCOME TO KBC \n") 
print( "HAVE A SEAT \n")
print ( "THE RULES OF THE GAME ARE AS FOLLOW :\n")
print ("1.THERE ARE 10 QUESTIONS IN THE GAME ")
print("2.EACH QUESTION HAS 4 OPTIONS")
print ("3.YOU HAVE RE TO SELECT A CORRECT OPTION ")
print ('4.EVERY CORRECT ANSWER WILL WIN YOU 10000 RUPEES\n')
print( "SO LETS BEGIN THE GAME")
n= [1,2,3,4,5,6,7,8,9,10]
p=["NIET","IET","NIT MANIPUR","NIT SILCHAR","NIT CALICUT","IIIT ALLAHABAD","IIT BHUBANESWAR","IIT HYDERABAD","IIT DELHI","IIT BOMBAY"]
q= ["what is the capital of india" , " delhi ",
    " mumbai ",
  " chandigrh",
  " banglore",
1]
q2=["what does integration of an equation represents","its curve","its area","area under its curves","lope of its curve",3]

q3=["what is the value of planks constant","8.85 x 10^24 \n",
      " 6.64x 10^34 \n",
    " 8 x 10^26\n",
    " none of the above",2]

q4=["A light of high wavelength will have "," low energy\n",
      " high energy \n",
    " high  speed \n",
    " low speed ",1]

q5 = [ " which is considered standard electrode potential", "oxidation potential\n",
        " reduction potential \n",
      " both \n",
      " none  ",2]

q6=["In which direction induced current will flow", "clock-wise\n",
      " anti-clockwise \n",
    " in direction that opposed its cause of production \n",
    " in direction that supports its cause of production ",3]

q7 =[ " An helium nucleus like particle (charge=2,mass=2) is emitted in ", "alpha decay\n",
       "beta decay \n",
     "both \n",
     "none ",1]

q8=["If we give an photon particle wprk function energy , will it emmit an electron ","may emmitv\n",
      " will not emmit\n",
    " will get absorbed \n",
    " will deflect  ",1]
q9=["To get max capacitance , 2 capacitors should be arranged in ","series\n",
      " parallel\n",
    " in shot circuit \n",
    " in open circuit  ",2]
q10=["An electron moving in a straight line when entered in an magnetic fiels will move in circular motion , if the magnetic field is  ","its direction of its velocity\n",
       "parallel to its velocity\n",
     "perpendicular to its velocity\n",
     "at ab angle to its velocity ",3]
ques= [ q,q2,q3,q4,q5,q6,q7,q8,q9,q10]
while True:
  for e in range(len(ques)):
   k=(f'Question number {n[e]} which is:')                
   print(f'{k} \n{ques[e][0]}? \nYour options are:\n1.{ques[e][1]}\n2.{ques[e][2]}\n3.{ques[e][3]}\n4.{ques[e][4]}') 
   print(f'{k}\n')
   i = int(input("Enter you answer"))
   if i==ques[e][5]:
    print(f'Correct answer✅ \n')
   else:
    print("Wrong answer❌")
    print(f'You Got Admitted To {p[e-1]}')
    break
  else:
    print(f"🎉 Congratulations! You've made it to  {p[-1]} !")
  print("Exam Over ✅")
  break
