class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        s = []

        for i in arr:
            s.append(abs(i - x))

        # Find index of minimum distance
        ind = s.index(min(s))

        res = [arr[ind]]

        left = ind - 1
        right = ind + 1

        
        while len(res) < k:

            if left < 0:
                res.append(arr[right])
                right += 1

            elif right >= len(arr):
                res.append(arr[left])
                left -= 1

            elif s[left] <= s[right]:
                res.append(arr[left])
                left -= 1

            else:
                res.append(arr[right])
                right += 1

        return sorted(res)