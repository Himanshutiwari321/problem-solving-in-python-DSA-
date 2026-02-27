#contiguous array


nums = [0,1,1,1,1,1,0,0,0]

prefix_sum = 0
sums = {0:-1}
max_lenght = 0

for i in range(len(nums)):
   if nums[i]==0:
      prefix_sum -= 1

   else:
      prefix_sum += 1

   if prefix_sum in sums:
      max_lenght = max(max_lenght,i - sums[prefix_sum])

   else:
      sums[prefix_sum]=i      
print(max_lenght)