class Solution:
    def pivotIndex(self, nums):
        
        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = total -left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]

        return -1

abj = Solution()
nums = [1,7,3,6,5,6]
print(abj.pivotIndex(nums))        