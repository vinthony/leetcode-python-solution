class Solution:
	# @param {integer[]} nums
	# @param {integer} k
	# @return {boolean}
	def containsNearbyDuplicate(self, nums, k):
		d = {}
		for x in range(0,len(nums)):
			if nums[x] in d:
				j = d[nums[x]]
				if abs(j-x) <= k:
					return True
			d[nums[x]] = x
		return False	        


if __name__ == '__main__':
	s = Solution().containsNearbyDuplicate([1,2,1],2)		
	print s