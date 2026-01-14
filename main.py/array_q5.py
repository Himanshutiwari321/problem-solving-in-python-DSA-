#majority element in a list 

nums = [7,7,5,2,5,7,7]

n = len(nums)

majority = {}

for i in nums:
  if i in majority:
    majority[i] = majority[i] + 1

  else:
    majority[i]=1

for i in majority:
  if majority[i] >= (n//2):
    print(i)
    break

    