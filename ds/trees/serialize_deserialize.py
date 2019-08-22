class Codec:

    def serialize(self, root):
        self.vals = []
        def encode(node):
            if node is not None:
                self.vals.append(str(node.val))
                encode(node.left)
                encode(node.right)
            else:
                self.vals.append("#")
        encode(root)
        return ' '.join(self.vals)

    def serialize_bfs(self, root):
        self.vals = []
        def encode(root):
            q = [root]
            while q:
                node = q.pop(0)
                if node is None:
                    continue
                self.vals.append(str(node.val))
                if node.left:
                    q.append(node.left)
                else:
                    self.vals.append('#')
                if node.right:
                    q.append(node.right)
                else:
                    self.vals.append('#')

        encode(root)
        return ' '.join(self.vals)

    def deserialize_bfs(self, data):
        vals = data.split()
        def decode(self, vals):
            root = TreeNode(vals[0])
            q = [root]
            while q:
                node = q.pop(0)
                val = vals.pop(0)
                if val == '#':
                    continue
                node = TreeNode(val)
                val.pop(0)
                if val == '#':
                    root.left = None
                else:
                    root.left = TreeNode(val)
                val = val.pop(0)
                if val == '#':
                    root.right = None
                else:
                    root.right = TreeNode(val)


    def deserialize(self, data):
        def decode(data):
            val = next(data)
            if val == '#':
                return None
            root = TreeNode(val)
            root.left = decode(data)
            root.right = decode(data)
            return root

        data = iter(data.split())
        return decode(data)
