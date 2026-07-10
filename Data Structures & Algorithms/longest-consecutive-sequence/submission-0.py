class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        store = set(nums)
        c = 0 
        longest = 0 
        for i in nums:

            if i - 1 not in store : 

                lenght = 1 

                while i + lenght in store : 

                    lenght += 1 
            
                longest = max(longest,lenght)

        return longest 


    
        