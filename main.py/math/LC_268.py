#print missing number in a array 

nums = [0,1,2,3,4,5,6,7,9]

n = len(nums)
print (n*(n+1)//2-sum(nums))
