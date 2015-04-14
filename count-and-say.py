class Solution:
	# @return a string
	def countAndSay(self, n):
		str1 = ""
		if n == 1 :
			return "1"
		arr = self.countAndSay(n-1);
		curr = ""
		count = 0
		for x in range(0,len(arr)):
			# print x ,arr[x]
			if curr == "":
				curr = arr[x];
			if curr == arr[x] :
				count = count + 1
			else:
				str1 = str1 + str(count) + curr
				curr = arr[x]
				count = 1
		return str1+str(count)+curr				

if __name__ == '__main__':
	s = Solution()
	print s.countAndSay(5)		