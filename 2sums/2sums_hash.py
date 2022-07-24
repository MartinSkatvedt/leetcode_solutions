class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        index_map = {}
        result = []


        for i, value in enumerate(nums):
            diff = target - value
            if diff in index_map:
                result.append(i)
                result.append(index_map[diff])
                break
            else:
                index_map[value] = i
        
        return result
