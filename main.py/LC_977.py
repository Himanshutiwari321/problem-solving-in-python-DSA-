#square of a sorted array  Asending order

nums = [-4,-1,0,3,10]

n = len(nums)
result = [0]*n

left = 0
right = n - 1
pos = n-1

while left <= right:
    if abs(nums[left]) > abs(nums[right]):
       result[pos]= nums[left]*nums[left]
       left= left+1

    else:  
       result[pos]= nums[right]*nums[right]
       right = right-1
    pos = pos -1

print(result)      