class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
# 快慢指针类型算法问题
# 定义快慢指针
# 快指针轮询数组
# 判断到快慢指针下标的值相同->快指针右移一位
# 判断到快慢指针下标的值不同->1 交换快慢指针对应的值，2 慢指针右移一位


