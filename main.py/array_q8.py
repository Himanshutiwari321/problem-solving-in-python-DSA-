# remove duplicate element in array --- list in python 

nums = [1,2,2,3,3,4,4]

left = 0

for right in range(1,len(nums)):
    if nums[left]!= nums[right]:
       left+=1
       nums[left]=nums[right]
       
print (left+1)
result = nums[:left+1]

print(result)