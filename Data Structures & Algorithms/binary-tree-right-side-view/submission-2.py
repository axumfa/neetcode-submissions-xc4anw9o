# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        q = deque([root])
        res = []
        
        while q:
            RightSide = None
            size = len(q)
            
            for i in range(size):
                node = q.popleft()
                if node:
                    RightSide = node
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            if RightSide:
                res.append(RightSide.val)

        return res