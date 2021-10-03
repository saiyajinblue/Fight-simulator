import random

vegeta = [1,3,5,7,9]
goku = [0,2,4,6,8]

v = 100
g = 100

while True:
   num = random.randint(1,9)
   if num in vegeta:
      v-=20
   else:
      g-=20
   print(f"vegeta power level: {v})
   print(f"goku power level: {g})
   if g==0:
      print("Vegeta won the fight")
      break
   else:
      print("Goku won the fight")
      break
