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
    Implements the recursive method for Binary Tree Preorder Traversal.
    Preorder sequence: Root -> Left -> Right
    """

    # Version 1: Traverse (Recursive Approach)
    # Type hints removed for maximum compatibility
    def preorderTraversal(self, root):
        """
        Main method to initiate the preorder traversal.

        Args:
            root: The root node of the binary tree.

        Returns:
            A list containing the values of the nodes in preorder sequence.
        """
        # A list to store the results of the traversal.
        results = []
        # Calls the recursive helper method to perform the traversal.
        self._traversal(results, root)
        return results

    # Type hints removed for maximum compatibility
    def _traversal(self, results, root):
        """
        Helper method to recursively traverse the tree.

        Args:
            results: The list to which node values are appended.
            root: The current node in the traversal.
        """
        # Base case for the recursion: if the current node is None (end of a branch),
        # we simply return and do nothing.
        if root is None:
            return

        # 1. Visit the root: Append the value of the current node to the results list.
        # This is the "pre" part of "preorder".
        results.append(root.val)

        # 2. Traverse the left subtree: Recursively call the traversal method on the left child.
        self._traversal(results, root.left)

        # 3. Traverse the right subtree: Recursively call the traversal method on the right child.
        self._traversal(results, root.right)


# --- Example Usage ---

# Build the tree for {1,#,2,3} -> [1, 2, 3]
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

root.right = node2
node2.left = node3

solver = Solution()
traversal_result = solver.preorderTraversal(root)

# Using the .format() method instead of f-string for compatibility
print("The preorder traversal result is: {}".format(traversal_result))
