class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)

        sample = [0] * n 

        for i in range(len(nums)) : 

            ind = (i+k) % n

            sample[ind] = nums[i] 


        for i in range(len(sample)):

            nums[i] = sample[i]


