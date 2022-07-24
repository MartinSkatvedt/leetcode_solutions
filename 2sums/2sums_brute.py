class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_length = len(nums)
        
        for i in range(nums_length):
            for j in range (nums_length):
                if (i == j):
                    continue
                if (nums[i] + nums[j] == target):
                     return [i, j]
