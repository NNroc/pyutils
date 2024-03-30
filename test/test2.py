# Definition for a binary tree node.

import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        ans = 0
        q = queue.Queue()
        q.put(root)
        while q.qsize() > 0:
            node = q.get()
            if node == None:
                continue
            else:
                q.put(node.left)
                q.put(node.right)
            ans += 1
        return ans


right = TreeNode(2)
root = TreeNode(1, None, right)
Solution.maxDepth(None, root)
