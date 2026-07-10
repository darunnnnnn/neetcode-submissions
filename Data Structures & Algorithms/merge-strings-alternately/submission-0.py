class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        r = ""

        a = 0 
        b = 0 

        while a < len(word1) and b < len(word2) :

            r = r + word1[a] + word2[b]
            a += 1 
            b += 1 

        if word1 : 

            r = r + word1[a:]
        if word2 :

            r = r + word2[b:]


        return r 

