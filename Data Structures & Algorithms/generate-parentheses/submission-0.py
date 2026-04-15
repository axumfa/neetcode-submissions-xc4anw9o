class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtracking(open_p,close_p):

            if open_p == close_p == n:
                res.append(''.join(stack))
                return
            
            if open_p < n:
                stack.append('(')
                backtracking(open_p + 1, close_p)
                stack.pop()
            
            if close_p < open_p:
                stack.append(')')
                backtracking(open_p,close_p + 1)
                stack.pop()
            
        backtracking(0,0)
        return res