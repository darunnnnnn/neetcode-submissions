class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        w = {c: i for i, c in enumerate(order)}

        for j in range(len(words) - 1):

            w1 = words[j]
            w2 = words[j + 1]

            for i in range(len(w1)):

                if i == len(w2):
                    return False

                elif w1[i] != w2[i]:

                    if w[w2[i]] < w[w1[i]]:
                        return False

                    break

        return True