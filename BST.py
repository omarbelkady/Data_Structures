class TreeNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value if value is not None else key
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        """Initialize an empty binary search tree"""
        self.root = None
        self.size = 0
    
    def __len__(self):
        """Return the number of nodes in the tree"""
        return self.size
    
    def is_empty(self):
        """Check if the tree is empty"""
        return self.size == 0
    
    def _find_node(self, key, node=None):
        """Find a node with the given key, starting from the given node or root"""
        if node is None:
            node = self.root
            
        if node is None:
            return None
        
        if key == node.key:
            return node
        elif key < node.key and node.left:
            return self._find_node(key, node.left)
        elif key > node.key and node.right:
            return self._find_node(key, node.right)
        
        return None
    
    def search(self, key):
        """Search for a key in the tree and return the associated value"""
        node = self._find_node(key)
        return node.value if node else None
    
    def _find_min_node(self, node):
        """Find the node with the minimum key in the subtree rooted at node"""
        current = node
        while current and current.left:
            current = current.left
        return current
    
    def _find_max_node(self, node):
        """Find the node with the maximum key in the subtree rooted at node"""
        current = node
        while current and current.right:
            current = current.right
        return current
    
    def find_min(self):
        """Find the minimum key in the tree"""
        if self.root is None:
            return None
        min_node = self._find_min_node(self.root)
        return min_node.value
    
    def find_max(self):
        """Find the maximum key in the tree"""
        if self.root is None:
            return None
        max_node = self._find_max_node(self.root)
        return max_node.value
    
    def insert(self, key, value=None):
        """Insert a key-value pair into the BST"""
        value = value if value is not None else key
        new_node = TreeNode(key, value)
        
        # If tree is empty, new node becomes root
        if self.root is None:
            self.root = new_node
            self.size += 1
            return
        
        current = self.root
        while True:
            # Key already exists, update the value
            if key == current.key:
                current.value = value
                return
            
            # Go left
            elif key < current.key:
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    self.size += 1
                    return
                current = current.left
            
            # Go right
            else:
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    self.size += 1
                    return
                current = current.right
    
    def _transplant(self, u, v):
        """Replace subtree rooted at node u with subtree rooted at node v"""
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
            
        if v is not None:
            v.parent = u.parent
    
    def delete(self, key):
        """Delete a node with the given key from the BST"""
        node = self._find_node(key)
        if node is None:
            return False
        
        # Case 1: Node has no left child
        if node.left is None:
            self._transplant(node, node.right)
        
        # Case 2: Node has no right child
        elif node.right is None:
            self._transplant(node, node.left)
        
        # Case 3: Node has both children
        else:
            # Find successor (smallest node in right subtree)
            successor = self._find_min_node(node.right)
            
            # If successor is not the right child of node
            if successor.parent != node:
                # Replace successor with its right child
                self._transplant(successor, successor.right)
                # Make node's right child the successor's right child
                successor.right = node.right
                successor.right.parent = successor
                
            # Replace node with successor
            self._transplant(node, successor)
            # Make node's left child the successor's left child
            successor.left = node.left
            successor.left.parent = successor
        
        self.size -= 1
        return True
    
    def _inorder_traversal(self, node, result):
        """Helper method for inorder traversal"""
        if node:
            self._inorder_traversal(node.left, result)
            result.append((node.key, node.value))
            self._inorder_traversal(node.right, result)
    
    def inorder_traversal(self):
        """Return a list of key-value pairs in sorted order"""
        result = []
        self._inorder_traversal(self.root, result)
        return result
    
    def _preorder_traversal(self, node, result):
        """Helper method for preorder traversal"""
        if node:
            result.append((node.key, node.value))
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)
    
    def preorder_traversal(self):
        """Return a list of key-value pairs in preorder"""
        result = []
        self._preorder_traversal(self.root, result)
        return result
    
    def _postorder_traversal(self, node, result):
        """Helper method for postorder traversal"""
        if node:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append((node.key, node.value))
    
    def postorder_traversal(self):
        """Return a list of key-value pairs in postorder"""
        result = []
        self._postorder_traversal(self.root, result)
        return result
    
    def _print_tree(self, node, level=0):
        """Helper method to print tree structure"""
        if node is not None:
            self._print_tree(node.right, level + 1)
            print(' ' * 4 * level + f"-> {node.key}")
            self._print_tree(node.left, level + 1)
    
    def print_tree(self):
        """Print the tree structure"""
        self._print_tree(self.root)

# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    
    # Insert some key-value pairs
    keys = [50, 30, 70, 20, 40, 60, 80]
    for key in keys:
        bst.insert(key)
    
    print("BST Structure:")
    bst.print_tree()
    
    print("\nInorder traversal (sorted):", bst.inorder_traversal())
    print("Preorder traversal:", bst.preorder_traversal())
    print("Postorder traversal:", bst.postorder_traversal())
    
    print("\nMinimum value:", bst.find_min())
    print("Maximum value:", bst.find_max())
    
    # Search for keys
    print("\nSearching for key 40:", bst.search(40))
    print("Searching for key 55:", bst.search(55))
    
    # Delete nodes
    print("\nDeleting node with key 30")
    bst.delete(30)
    print("BST after deletion:")
    bst.print_tree()