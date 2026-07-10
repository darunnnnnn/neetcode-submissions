class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        si = {}
        ti = {}

        for i in s : 

            si[i] = 1 + si.get(i,0)

        for j in t: 

            ti[j] = 1 + ti.get(j, 0)

        return ti==si






