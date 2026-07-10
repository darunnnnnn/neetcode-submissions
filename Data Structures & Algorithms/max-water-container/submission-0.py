class Solution:
    def maxArea(self, heights: List[int]):

        l = 0
        r = len(heights) - 1

        area = 0

        while l < r:

            carea = min(heights[l], heights[r]) * (r - l)

            area = max(area, carea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return area