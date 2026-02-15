# push one 

nums = [9,9,9]

for i in range(len(nums)-1,-1,-1):
    if nums[i]<9:
      nums[i]+=1
      break
    nums[i]=0
else:
   nums = [1]+nums

print(nums)   
  