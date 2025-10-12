n= int(input("Enter the number of rounds you want to play :"))
i=1
users_points=0
while i<=n:
  c = [0,1,2]
  import random 
  u= random.choice(c)
  o=int(input(f"Enter your choice for round {i}\n 0 for Snake\n 1 for Water\n 2 for Gun\n  your choice is : " ))
  d="⚖️ This round was draw ⚖️"
  w="🎉 You won this round 🎉"
  l="😵 You loose this round 😵"
  matrix = [
    [d, w, l],
    [l, d, w],
    [w, l, d]
  ]
  print(f"The computer's choice was : {u} ")
  print ("                                               ")
  print(matrix[o][u])
  print ("                                                 ")
  i=i+1
  if matrix[o][u] == w:
    users_points = users_points+1
print(f"your total points are : {users_points}")
if users_points>n:
    print("🎉 You Won The Game 🎉")
elif users_points ==n:
    print("⚖️ The Game Was A Draw ⚖️")
else:
  print("😵 You Loose The Game 😵")
print("🏁 GAME OVER 🏁")