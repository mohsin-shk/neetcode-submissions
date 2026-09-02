class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        h = set()
        maxLen = 0
        l,r=0,0
        while r<n:
            while s[r] in h:
                h.remove(s[l])
                l += 1
            maxLen =  max(maxLen,r-l+1) 
            h.add(s[r])
            r += 1
        
        return maxLen


