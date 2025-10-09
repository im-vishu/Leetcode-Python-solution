# Definition for a binary tree node.
class TreeNode:
    """
    Represents a node in a binary tree.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ---

class Solution:
    """
    Implements the iterative method for Binary Tree Inorder Traversal using a Stack.
    Inorder sequence: Left -> Root -> Right
    """

    def inorderTraversal(self, root):
        """
        Performs iterative inorder traversal.
        """
        # Python list acts as the stack (LIFO: Last In, First Out)
        stack = []
        # List to store the results (traversed node values)
        results = []

        # The loop continues as long as there are nodes to process or nodes in the stack
        while stack or root:
            # 1. Traverse as far left as possible, pushing nodes onto the stack
            if root:
                stack.append(root)
                root = root.left
            else:
                # 2. Left child is None. Pop the last node (Root)
                root = stack.pop()
                
                # 3. Visit the Root node
                results.append(root.val)
                
                # 4. Move to the Right child and repeat the process (start at step 1)
                root = root.right
        
        return results

# --- Example Usage ---

# Build the tree for {1,#,2,3}
# Structure: 1 -> right 2 -> left 3
# Expected Inorder output (Left, Root, Right): [1, 3, 2]

root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

root.right = node2
node2.left = node3

solver = Solution()
traversal_result = solver.inorderTraversal(root)

# Using the .format() method for maximum compatibility
print("The inorder traversal result is: {}".format(traversal_result))
