class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)


        for s in strs : 

            l = [0] * 26

            for ch in s : 

                l[ord(ch) - ord('a')] += 1 
            
            res[tuple(l)].append(s)

        return list(res.values())