#subarray sum equal k 

nums = [1,2,1,2,1]
k = 3

count = 0 
c_sum = 0

sums = {0:1}

for num in nums :
   c_sum+=num
   if c_sum-k in sums:
      count+=sums[c_sum-k]

   sums[c_sum] = sums.get(c_sum,0)+1

print(count)     