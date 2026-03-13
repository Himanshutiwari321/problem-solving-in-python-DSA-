#remove duplicates 
#Brutefource solution

nums = [0,0,1,1,1,2,2,3,3,4]
if not nums:
   print(nums)
ans = []
for left in range(len(nums)-1):
    for right in range(left+1,left+2):
        if nums[left]!= nums[right]:
           ans.append(nums[left])
ans.append(nums[-1])

print(ans)  

#optimize solution o(n)
nums = [0,0,1,1,1,2,2,3,3,4]

if not nums:
   print(nums)

left = 0

for right in range(1,len(nums)):
   if nums[left]!=nums[right]:
      left+=1
      nums[left]=nums[right]


print(nums[:left+1])
print(left+1)      

