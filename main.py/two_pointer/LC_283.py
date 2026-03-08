# moves zeroz

nums =[0,1,0,3,12]

first = 0

for n in nums:
  if n!= 0:
    nums[first]=n
    first+=1
    
while first < len(nums):
    nums[first]=0
    first+=1
print(nums)
       