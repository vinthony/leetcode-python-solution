#!/usr/bin/env python

class Solution:
    # @return a list of integers
    def exp(self,y):
    	s = 1;
    	while y > 0:
    		s = s * y
    		y = y - 1	
    	return s

    def getRow(self, rowIndex):
    	#[0...n]
    	arr = [];
    	for x in range(0,rowIndex+1):
    		if x == 0 or x == rowIndex:
    			arr.append(1)
    		else:
    			arr.append(self.exp(rowIndex)/(self.exp(x)*self.exp(rowIndex-x)))	
    	return arr;
    	
if __name__ == "__main__":
	s = Solution();    			
	print s.getRow(4);
