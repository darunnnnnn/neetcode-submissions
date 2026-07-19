# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def issame(p,q):

            if not p and not q : 

                return True 

            if p and not q or not p and q : 

                return False 

            if p.val != q.val : 

                return False 

            return issame(p.right,q.right) and issame(p.left,q.left)
        

        def ch(node):

            if not node : 
                return False 


            if issame(node,subRoot):

                return True 

            
            return ch(node.right) or ch(node.left)


        return ch(root)