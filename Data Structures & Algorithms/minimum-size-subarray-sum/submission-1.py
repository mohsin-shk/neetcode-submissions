class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # brute
        res = float("inf")
        for  i in range(len(nums)):
            Sum = 0
            for j in range(i,len(nums)):
                Sum += nums[j]
                if Sum >= target:
                    res =  min(res,j-i+1)
                    break
        
        return 0 if res == float("inf") else res
                