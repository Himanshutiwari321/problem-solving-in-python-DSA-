#two sum problem using hash map


nums = [2,7,11,15]
target = 9
seen = {}

for i in range (len(nums)):
    cur = nums[i]
    com = target - cur
    if com in seen:
       print(seen[com],i)
    else:
        seen[cur]=i

    
    


         
      

