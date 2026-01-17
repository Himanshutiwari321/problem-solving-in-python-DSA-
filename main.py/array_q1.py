#two sum problem using hash map


nums = [2,7,11,15]
target = 9
seen = {}

for i in nums:
    
    com = target - i
    if com in seen:
       print(seen[com],i)
    else:
        seen[i] = i


# print index value == target 

nums = [2,7,11,15]
target = 9
seen = {}
        
for i in range (len(nums)):
    cur = nums[i]
    comm = target - cur 
    if comm in seen:
        print(seen[comm],i )

    else:
        seen[cur] = i        

    
    


         
      

