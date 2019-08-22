def lca(root, p, q):
    if root == p or right == q:
        return root

    left = right = None
    if root.left:
        left = self.lca(root.left, p, q)
    if root.right:
        right = slef.lca(root.right, p, q)

    if left and right:
        return root
    else:
        return left or right

