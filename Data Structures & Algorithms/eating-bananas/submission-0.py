class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        a = 1
        b = max(piles)

        k = b

        while a <= b:

            m = (a + b) // 2

            hr = 0

            for i in piles:
                hr += math.ceil(i / m)

            if hr <= h:
                k = m
                b = m - 1
            else:
                a = m + 1

        return k