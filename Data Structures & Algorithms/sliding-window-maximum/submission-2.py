class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # res = []
        # l = 0
        # for r in range(k-1,len(nums)):
        #     maxi = max(nums[l:r+1]) 
        #     # we are checking this max again and again for whole window -> maybe we can do some optimization 
        #     res.append(maxi)
        #     while (r-l+1)==k:
        #         l+=1
        
        # return res

        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):

            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if(r+1)>=k:
                output.append(nums[q[0]])
                l+=1
            
            r+=1
        
        return output

        
        
            
                