class Solution:
    def mySqrt(self, x: int) -> int:
        

        a = 1 
        b = x 

        while a <= b : 

            mid = (a + b ) // 2 

            if mid ** 2 > x : 

                b = mid - 1 

            elif mid ** 2 < x : 

                a = mid + 1 

            else : 

                return mid 

        return  b 