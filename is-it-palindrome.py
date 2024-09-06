# TRY 1
def isPalindrome(self, x: int) -> bool:
	#convert to a string 
	num_str = str(x)
	for i in range(0, len(num_str)//2):
		if num_str[i] != num_str[len(num_str)-i-1]:
			return False
	return True