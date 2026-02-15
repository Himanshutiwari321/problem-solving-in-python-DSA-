# push one 

nums = [1,2,3]

for i in range(len(nums)-1,-1,-1):
    if nums[i]<9:
       nums[i]+=1
    print(nums)
    break  


nums[i]=0   