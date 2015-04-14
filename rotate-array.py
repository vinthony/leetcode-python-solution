class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
    	lens = len(nums)
    	nums[:]= nums[lens-k:lens]+nums[0:lens-k]
    	print nums
    def rotate2(self,nums,k):
    	lens = len(nums)
    	if k == 0 and k != 1:
    		return
    	if lens < k :
    		k = k - lens		
    	for i in xrange(0,lens-k):
    		nums.append(nums[i])
    	del nums[0:lens-k]	
    	print nums

if __name__ == '__main__':
	s = Solution()
	s.rotate2([1,2],0)    	