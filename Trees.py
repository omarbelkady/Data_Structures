class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    # Insert
    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert(self.root, val)
    
    def _insert(self, node, val):
        if val < node.val:
            if not node.left:
                node.left = TreeNode(val)
            else:
                self._insert(node.left, val)
        else:
            if not node.right:
                node.right = TreeNode(val)
            else:
                self._insert(node.right, val)
    
    # Search
    def search(self, val):
        return self._search(self.root, val)
    
    def _search(self, node, val):
        if not node:
            return False
        if node.val == val:
            return True
        elif val < node.val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)

# Example Usage:
bst = BST()
bst.insert(5)
bst.insert(3)
bst.search(3)  # Returns True