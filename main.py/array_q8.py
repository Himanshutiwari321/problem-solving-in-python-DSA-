# remove duplicate element in array --- list in python 

nums = [1,2,2,3,3,4,4,4,5,7,6,]

result = []

for i in nums:
  if i not in  result:
     result+= [i]  # result.append(i) ye code bhi kam karega  list mai ye code use kar sakte hai append karne ke liye 

print(result )  
