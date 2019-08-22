class Solution:

    def search(self, root, x, path):
        if not root or path:
            return
        if root.val == x:
            path.append(root)
            return
        self.search(root.left, x, path)
        self.search(root.right, x, path)
        if path:
            path.append(root)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        left_path, right_path = [], []
        self.search(root, p.val, left_path)
        self.search(root, q.val, right_path)
        p1, p2 = left_path.pop(), right_path.pop()
        prev = None
        while p1.val == p2.val and len(left_path) > 0 and len(right_path) > 0:
            prev = p1
            p1, p2 = left_path.pop(), right_path.pop()
        if p1 == p2:
            return p1
        return prev


