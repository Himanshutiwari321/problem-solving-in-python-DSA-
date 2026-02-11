#find duplicate item from list.

nums = [1,2,3,22]
result = {}

for i in nums:
   if i in result:
      result[i]+=1

   else:
      result[i]=1

for i in result:
   if result[i]!= 1:
      print(True)
      break
else:
   print(False)  
      
