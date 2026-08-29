class Solution:
    def reverseArr(self,nums:List[int],start:int,end:int)->List[int]:
        while start<end:
            nums[start],nums[end] = nums[end],nums[start]
            start += 1
            end -= 1
        
        return nums


    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k =  k % n
        self.reverseArr(nums,0,n-1)
        self.reverseArr(nums,0,k-1)
        self.reverseArr(nums,k,n-1)
        

        
        