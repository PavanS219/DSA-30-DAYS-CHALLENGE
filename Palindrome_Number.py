class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        return True if a[::-1] == str(x) else False
        
