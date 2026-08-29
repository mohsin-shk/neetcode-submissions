class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # n = len(heights)
        # area = float("-inf")
        # for i in range(n):
        #     for j in range(i+1,n):
        #         maxH = min(heights[i],heights[j])
        #         maxW = j - i
        #         area =  max(area,maxH*maxW)
        
        # return area

        l,r = 0,len(heights)-1
        area = 0
        while l<r:
            area = max(area,(r-l)*min(heights[l],heights[r]))
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1

        return area           


