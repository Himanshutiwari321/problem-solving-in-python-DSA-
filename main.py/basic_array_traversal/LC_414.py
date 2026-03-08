#third maximum number in list 

#nums = [1,2]
nums = [2,2,3,1]

first = second = third = None

for n in set(nums):
   if first is None or n > first:
       third = second 
       second = first 
       first  = n

   elif second is None or n > second:
       third = second 
       second = n

   elif third is None or n > third:
       third = n    

#if third is None :
   # print (first)
#else:
    #print (third) 


print(nums.index(first))
print(second)
print(third )       


