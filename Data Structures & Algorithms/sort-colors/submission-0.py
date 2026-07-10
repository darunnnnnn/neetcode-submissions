class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []
        de = Counter(nums)

        red =de[0]
        white=de[1]
        blue=de[2]

        

        i = 0 
        r = 0 
        while r < red : 

            nums[i] = 0 
            i += 1 
            r += 1 

        r = 0 

        while r < white : 

            nums[i] = 1 
            i += 1 
            r += 1 

        r = 0 

        while r < blue : 

            nums[i] = 2 
            i+= 1 
            r += 1 


        



            