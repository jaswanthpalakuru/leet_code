class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = ''
        for i in s:
            if i.isalnum():
                b = b + i.lower()
        if(b == b[::-1]):
            return True
        else:
            return False