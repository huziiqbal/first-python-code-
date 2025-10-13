# #QUESTIONS BASED ON OOP
 
# #NUMBER 1

class Car :
  def __init__(self,brand,model,year):
    self.brand = brand
    self.model = model
    self.year = year
  def info(self):
    print(f'Today We are talking about {self.brand} {self.model} which was launched in {self.year}')

no1 = Car("BMW","X5",2020)
no2 = Car("toyota","fortuner",2022)

no1.info()
no2.info()

# # NUMBER 2

class Rectangle:
  def __init__(self,length, width):
    self.length = length
    self.width  = width

  def area(self):
   print(f'The area of the rectangle with dimentions you gave is {self.length * self.width}')

first_figure = Rectangle(10,23)
second_figure = Rectangle(34,73)

first_figure.area()
second_figure.area()

#IMPROVED NUMBER 2 

class Rectangle:
  def __init__(self,length, width):
    self.length = length
    self.width  = width

  def area(self):
   print(f'The area of the rectangle with dimensions you gave is {self.length * self.width}\n')

while True:

    l=int(input("enter the length of the rectangle you want area of "))
    w=int(input("enter the width of the rectangle you want area of "))
   
    first_figure = Rectangle(l,w)
    first_figure.area()
    
    t=int(input("Do you want area of another rectangle ?\n" "if yes then press 1 and if no then press 0 " ))
    if t==0:
       break