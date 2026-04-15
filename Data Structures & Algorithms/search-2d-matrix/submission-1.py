class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][-1] < target:
                continue
            
            else:
                left, right = 0, len(matrix[i])
                while left <= right:
                    mid = left + (right - left) // 2

                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        right = mid - 1
                    elif matrix[i][mid] < target:
                        left = mid + 1
                return False
        return False