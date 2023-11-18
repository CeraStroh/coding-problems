# Determine if string is a palindrome
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(e.lower() for e in s if e.isalnum())
 
        if s == s[::-1]:
            return True
        else:
            return False