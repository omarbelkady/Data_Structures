from collections import deque
class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    # Insert
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)
    
    def _insert(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        else:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)
    
    # Search
    def search(self, value):
        return self._search(self.root, value)
    
    def _search(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def inorder(self):
        self._inorder(self.root)
    def _inorder(self,node):
        if node is not None:
            self._inorder(node.left)
            print(node.value, end=" ")
            self._inorder(node.right)
    def preorder(self):
        self._preorder(self.root)
    def _preorder(self, node):
        if node is not None:
            print(node.value, end=" ")
            self._preorder(node.left)
            self._preorder(node.right)
    def postorder(self):
        self._postorder(self.root)
    def _postorder(self, node):
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.value, end=" ")
    def bfs(self):
        if not self.root:
            return
        queue=deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            print(node.value, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()
    
    def dfs(self):
        if not self.root:
            return
        stack=[self.root]
        while stack:
            node = stack.pop()
            print(node.value, end=" ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        print()


# Example Usage:
bst = BST()
bst.insert(5)
bst.insert(3)
bst.search(3)  # Returns True
bst.insert(4)
bst.insert(7)

bst.inorder()
bst.preorder()
bst.postorder()
