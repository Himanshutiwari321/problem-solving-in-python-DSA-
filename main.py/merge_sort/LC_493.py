# reverse pair    left is greter than 2*right 


nums = [1,3,2,3,1]

n = len(nums)

left = 0

count = 0

while left < n:
   right = left +1

   while right < n:
      if nums[left] > 2 * nums[right]:
        count += 1
      right += 1
            
   left += 1
print(count) 