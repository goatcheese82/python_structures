# This class will give us all the functionality we need to create a BST and traverse it using in-order, pre-order and post-order methods.

# We first create the constructor, which will initialize with no data unless provided. We will also set its pointers to None, as we have not added those nodes to the tree.

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

    ################
    # Problem 1    #
    ################
    """
    This function will traverse the tree to find the node of least value and return that value.
    """
    def get_min(self):
        pass

    ################
    # End Problem 1#
    ################

    ################
    #  Problem 2   #
    ################
    """
    This function will traverse the tree to find the node of greatest value and return that value.
    """


    def get_max(self):
        pass


    ################
    # End Problem 2#
    ################

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

bst = BST(27)
bst.insert(30)
bst.insert(38)
bst.insert(26)
bst.insert(72)


print(bst.get_min())
print(bst.get_max())