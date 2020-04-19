class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for index,value in enumerate(nums):
            dic[value] = index
        for i in range(len(nums)):
            tmp = target - nums[i]
            j = dic.get(tmp)
            if j is not None and i != j:
                return [i, j]
