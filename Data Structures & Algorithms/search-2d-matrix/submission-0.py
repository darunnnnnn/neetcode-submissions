class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        a = 0
        b = len(matrix) - 1

        col = len(matrix[0]) - 1

        while a <= b:

            mid = (a + b) // 2

            if matrix[mid][col] < target:
                a = mid + 1

            elif matrix[mid][0] > target:
                b = mid - 1

            else:

                x = 0
                y = col

                while x <= y:

                    m = (x + y) // 2

                    if matrix[mid][m] > target:
                        y = m - 1

                    elif matrix[mid][m] < target:
                        x = m + 1

                    else:
                        return True

                return False

        return False