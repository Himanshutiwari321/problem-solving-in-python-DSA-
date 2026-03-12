#maximum subarray
#bruteforce solution 0(n2)
nums = [-2,1,-3,4,-1,2,1,-5,4]
max_sum = nums[0]

for i in range (len(nums)):
    curr_sum = 0

    for j in range (i,len(nums)):
        curr_sum+=nums[j]
        if curr_sum>max_sum:
            max_sum=curr_sum
       
print(max_sum)                



#optimize solution using kadane algorithm 0(n)
nums = [-2,1,-3,4,-1,2,1,-5,4]

current_sum = 0
max_sum = nums[0]

for i in range (len(nums)):
           
    current_sum +=nums[i]
    if current_sum>max_sum:
        max_sum=current_sum
    if current_sum<0:
        current_sum = 0    

print(max_sum)  