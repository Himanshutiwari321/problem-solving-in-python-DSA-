# in array max consicutive ones 

num = [1,0,1,1,1,0,1,1]
count = 0
maxs = 0
for i in range(len(num)):
    if num[i]==1:
        count+=1
    elif num[i] == 0:
      maxs = count
      count = 0
if count>maxs:  
  print(count) 
elif maxs>count:
  print(maxs)      
   


# second way to solve this question 


nums = [1,0,1,1,1,0,1,1,1,1,1,1,1,1,1]

counts = 0
max_count = 0

for i in range(len(nums)):
    if nums[i] == 1:
        counts += 1
    else:
        max_count = max(max_count, counts)
        counts = 0

# loop ke baad final check
max_count = max(max_count, counts)

print(max_count)
