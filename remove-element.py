class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
    	m = 0
    	for x in range(0,len(A)):
    		if A[x] != elem:
    			A[m] = A[x]
    			m = m + 1
    	return m		

if __name__ == "__main__":
	s = Solution()
	print s.removeElement([4,1,2,3,4,5],4)     