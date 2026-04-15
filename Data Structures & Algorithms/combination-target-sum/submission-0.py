class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        path = []

        def dfs(i, curSum):

            if curSum > target:
                return

            if i >= len(nums):
                if curSum == target:
                    res.append(path.copy())
                return
            
            path.append(nums[i])
            curSum += nums[i]
            dfs(i, curSum)

            path.pop()
            curSum -= nums[i]
            dfs(i + 1, curSum)

            

        dfs(0, 0) 
        return res