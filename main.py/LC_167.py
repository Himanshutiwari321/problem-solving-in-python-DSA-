# two sum 2

nums= [2,7,11,15]
target = 9

left = 0
right = len(nums)-1

while left<right:
   sum1=nums[left]+nums[right]
   if sum1==target:
      print(left+1,right+1)
      break
   elif sum1>target:
      right-=1
   else:
      left+=1
         

         