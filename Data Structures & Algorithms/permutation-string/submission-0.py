class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        if len(s1) > len(s2) : 

            return False


        a = [0] * 26 
        b = [0] * 26
        


        for i in range(len(s1)) :

            a[ord(s1[i]) - ord('a')] += 1 
            b[ord(s2[i]) - ord('a')] += 1 

        if a == b : 

            return True 

        
        left = 0 

        for i in range(len(s1),len(s2)): 

            b[ord(s2[i]) - ord('a') ] += 1 

            b[ord(s2[left])- ord('a')] -= 1 

            if a == b : 

                return True 
            
            left += 1 

        return False 

