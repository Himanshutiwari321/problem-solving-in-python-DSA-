#two sum problem using hash map
   
class Solution:
    def twoSum (self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in seen:
                return seen[x],i
            seen[num]= i     

             

nums = [2,7,11,15]
target = 9

ret = Solution().twoSum(nums, target)
print(ret)
    
    


         
      

