#given intere are armstrong or not .

n = 153

num = n 
nod = len(str(n))
total = 0

while num > 0:
  id  = num % 10
  total = total + (id**nod )
  num = num //10

if total == n:
  print ("yes armstrong number ")

else:
  print ("no armstrong number")




