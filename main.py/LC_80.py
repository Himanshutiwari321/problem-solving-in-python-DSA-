# Remove Duplicates from Sorted Array || leetcode 80
#bruteforce solution 
nums = [1,1,1,2,2,3]

if len(nums)<=2:
   print(nums)
ans = []
for left in range(len(nums)-1):
    for right in range(left+1,left+2):
        if nums[left]!= nums[right]:
           ans.append(nums[left])
        else:
            if ans.count(nums[left]) < 2:
                ans.append(nums[left])
   
ans.append(nums[-1])

print(ans)  



nums = [1,1,1,2,2,3]
if len(nums)<= 2:
   print(nums)

left = 1
for right in range(2,len(nums)):
  
    if nums[right]!= nums[left-1]:
       left+=1
       nums[left]=nums[right]

print(left + 1)
print(nums[:left+1]) 