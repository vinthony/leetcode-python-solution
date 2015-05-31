class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        dic = {}
        for x in range(len(nums)):
        	if nums[x] in dic:
        		return True
        	dic[nums[x]] = x	
        return False	