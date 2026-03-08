class Solution:
    def dominantIndex(self, nums):
        
        first = None 
        second= None 
        for n in set(nums):
            if first is None or n > first:
                if n != first:
                  second = first 
                  first = n

            elif (second is None or n > second ) and n != first :
                second = n

        
        if second is not None and first >= 2 * second:
           return nums.index(first)

        return -1
    
abj = Solution()
nums = [3,6,1,0]
print(abj.dominantIndex(nums))  