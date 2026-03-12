# Remove Duplicates from Sorted Array || leetcode 80

nums = [1,1,1,2,2,3]
if len(nums)<= 2:
   print(nums)

left = 1
for right in range(2,len(nums)):
  
    if nums[right]!=nums[left-1]:
       left+=1
       nums[left]=nums[right]

print(left + 1)
print(nums[:left+1]) 