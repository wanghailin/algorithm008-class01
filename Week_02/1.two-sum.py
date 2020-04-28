class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for key, value in enumerate(nums):
            dic[value] = key

        for i in range(len(nums)):
            tmp = target - nums[i]
            j = dic.get(tmp)
            if j and j != i:
                return [i, j]