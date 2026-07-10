class Solution:
    def sortColors(self, nums: List[int]) -> None:

        l = 0
        r = len(nums) - 1
        j = 0

        while j <= r:

            if nums[j] == 0:

                nums[l], nums[j] = nums[j], nums[l]

                l += 1
                j += 1

            elif nums[j] == 1:

                j += 1

            else:

                nums[r], nums[j] = nums[j], nums[r]

                r -= 1