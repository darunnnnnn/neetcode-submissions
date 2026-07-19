class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        

        a = max(weights)
        b = sum(weights)
        res = b
        

        while a <= b : 

            cap = (a + b)//2 

            curcap = cap 
            ships = 1

            for i in weights : 

                

                if curcap < i : 

                    ships += 1 
                    curcap = cap 

                curcap -= i 
                

            if ships > days : 

                a = cap + 1 

            else : 

                res = min(res,cap)
                b = cap - 1 

        return res







