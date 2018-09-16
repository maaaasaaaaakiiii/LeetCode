from itertools import product

class Solution:

    def twoSum(self, nums, target):

        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in nums:
                return [i, nums.index(pair)]
