class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {'}' : '{', ')' : '(', ']' : '['}

        for char in s:
            if char in hash_map:
                if not stack or stack[-1] != hash_map[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return not stack        