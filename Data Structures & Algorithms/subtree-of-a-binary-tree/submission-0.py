# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if not subRoot:
            return True 
        
        stack1 = deque([root])
        
        while stack1:
            t = stack1.popleft()
            if self.sameTree(t, subRoot):
                return True
            
            stack1.append(t.left) if t.left else None
            stack1.append(t.right) if t.right else None
        
        return False

    
    def sameTree(self, p, q):
        stack = deque([(p, q)])

        while stack:
            n1, n2 = stack.popleft()

            if not n1 and not n2:
                continue
            elif (not n2 or not n1) or n1.val != n2.val:
                return False
            
            stack.append((n1.right, n2.right))
            stack.append((n1.left, n2.left))
        

        return True
