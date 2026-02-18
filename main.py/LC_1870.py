#minimum speed to arrive on time 
import math
nums  =[1,3,2]
hour =6

left = 1
right = 10**7

while left <= right:
   mid = (left+right)//2
   time = 0


   for i in range(len(nums)):
      if i == len(nums)-1:
         time = time +nums[i]/ float(mid)

      else:
         time = time + math.ceil(nums[i])/ float(mid)

   if time<=hour:
      right = mid -1

   else:
      left = mid+1 

print(left)                 