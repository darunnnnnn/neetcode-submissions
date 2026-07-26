# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def dfs(node,high) : 

            if not node :

                return 0 
            
            if node.val >= high : 

                res = 1

            else : 

                res = 0 

            high = max(high,node.val)
            res += dfs(node.left,high)
            res += dfs(node.right,high)

            return res 

        
        return dfs(root,root.val)



            
            
        