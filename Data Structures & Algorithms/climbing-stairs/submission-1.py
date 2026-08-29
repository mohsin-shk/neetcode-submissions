class Solution:
    
    def climbStairs(self, n: int) -> int:
        # if n == 0:
        #     return 1
        # if n == 1:
        #     return 1
        # l = self.climbStairs(n-1)
        # r = self.climbStairs(n-2)
        # return l+r

        prev = 1
        prev2 = 1

        for i in range(2,n+1):
            cur = prev + prev2
            prev2 = prev
            prev = cur
        return prev