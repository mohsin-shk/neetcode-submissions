class Solution:
    def mySqrt(self, x: int) -> int:
        # idea is sqr root of any number will always be in range of 
        # 1 and that number
        #  eq. sqr root of 8  will is 4 in range 1 - 8 
        #  now that I know range , and its sorted , I can maybe use binary search
        #  to check if any value in range 1 - x squares to x.
        #  if the square of the value is more we move left
        #  and vice versa

        l = 1
        h = x

        while l<=h:
            # assuming x is the sqr root value
            m =  (l+h)//2
            if m*m < x:
                l = m + 1
            elif m*m > x:
                h = m - 1
            elif m*m == x:
                return m

        return h
        