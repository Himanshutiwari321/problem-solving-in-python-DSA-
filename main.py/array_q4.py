# reverse a number  and check palidrome or not  

n = 123654
num = n
rev = 0

while num > 0:
  id = num %10
  rev= (rev*10)+id 
  num = num // 10 
if rev == num :
  print ("palidrom")
else:
  print("not palidrome")  



  