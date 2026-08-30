class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        l,r = 0,n-1
        cnt = 0
        while l<=r:
            rem = limit - people[r]
            r -= 1
            cnt += 1
            if l<=r and rem >= people[l]:
                l +=1
        return cnt
            

            
