class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:


        dic = Counter(nums)

        res = []


        for i in dic : 

            if dic[i] > len(nums) // 3 :

                res.append(i)

        return res 
        
        