class Solution:
    def isAlphaNum(self,ch):
        if 48<=ord(ch)<=57 or 97<=ord(ch)<=122 or 65<=ord(ch)<=90:
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        while l<r:
            while l<r and not self.isAlphaNum(s[l]):
                l += 1
            while l<r and not self.isAlphaNum(s[r]):
                r -= 1
                
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        
        return True