import random
import sleep

v = 100
g = 100

print("vegeta power level: ", v)
print("goku power level:   ", g)
print()
while True:
   sleep(2)
   num = random.randint(1,10)
   if num %2 == 0:
      v-=20
   else:
      g-=20
   print("vegeta power level: ", v)
   print("goku power level:   ", g)
   if g==0:
      print("\nVegeta is winner!")
      break
   if v==0:
      print("\nGoku is winner!")
      break
