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
  matrix = [[d, w, l],
            [l, d, w],
            [w, l, d]]
  print(f"The computer's choice was : {u} \n")
  print(f'{(matrix[o][u])}\n')
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

#UPDATED VERSION 

import random

print("🐍💧🔫 Welcome to the Snake-Water-Gun Game! 💥\n")

n = int(input("🎮 Enter the number of rounds you want to play: "))
users_points = 0
comp_points = 0

choices = ["Snake", "Water", "Gun"]

for i in range(1, n + 1):
    print(f"\n----- ROUND {i} -----")
    print("Your options: \n0️⃣ Snake\n1️⃣ Water\n2️⃣ Gun")
    try:
        o = int(input("👉 Enter your choice (0/1/2): "))
        if o not in [0, 1, 2]:
            print("⚠️ Invalid choice! Please enter 0, 1, or 2.")
            continue
    except ValueError:
        print("⚠️ Please enter a valid number!")
        continue

    u = random.choice([0, 1, 2])  # computer choice

    print(f"\n🧠 Computer chose: {choices[u]}")
    print(f"🧍 You chose: {choices[o]}")

    d = "⚖️ This round was a draw ⚖️"
    w = "🎉 You won this round 🎉"
    l = "😵 You lost this round 😵"
