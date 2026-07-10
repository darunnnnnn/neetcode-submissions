class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        a = 0 
        b = len(s) - 1 

        while a < b : 

            if s[a] != s[b] :

                lr = s[a+1 : b + 1 ]
                rr = s[a:b]

                return (lr == lr[::-1] or rr == rr[::-1])
            
            a += 1 
            b -= 1 

        return True 