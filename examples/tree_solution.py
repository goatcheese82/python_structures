class BST:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if not self.data:
            self.data = data
            return

        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left.insert(data)
                return
            self.left = BST(data)
            return

        if self.right:
            self.right.insert(data)
            return
        self.right = BST(data)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.data

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.data

    def preorder(self, datas):
        if self.data is not None:
            datas.append(self.data)
        if self.left is not None:
            self.left.preorder(datas)
        if self.right is not None:
            self.right.preorder(datas)
        return datas

    def inorder(self, datas):
        if self.left is not None:
            self.left.inorder(datas)
        if self.data is not None:
            datas.append(self.data)
        if self.right is not None:
            self.right.inorder(datas)
        return datas

    def postorder(self, datas):
        if self.left is not None:
            self.left.postorder(datas)
        if self.right is not None:
            self.right.postorder(datas)
        if self.data is not None:
            datas.append(self.data)
        return datas
