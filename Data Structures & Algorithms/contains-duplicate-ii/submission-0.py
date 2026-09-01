class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # its basically asking if in a k+1 size window return true if you find duplicate else just return false
        # why k + 1 ?
        #                         0 1 2 3
        #  for example array is  [1,2,3,1]  k=3 
        #  j = 3 and i = 0 => 3-0 = 3 , but the actual window is the portion from 0-to 3 making it of length 4 -> k+1
        # we can use hashet to check if a value came twice and within the window length and thus return the true.

        window = set()
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
        
        return False