class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        dic = Counter(nums)

        for i in dic : 

            if dic[i] > len(nums)// 2 : 

                return i 
        