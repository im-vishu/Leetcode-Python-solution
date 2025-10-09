class Solution:
    def sortedArrayToBST(self, nums):
        """
        Converts a sorted array into a height-balanced binary search tree (BST).
        
        Args:
            nums (list[int]): A sorted list of unique integers.
            
        Returns:
            TreeNode: The root of the constructed height-balanced BST.
        """
        def convert(left, right):
            """
            A recursive helper function to build the BST.
            
            Args:
                left (int): The left boundary of the current subarray.
                right (int): The right boundary of the current subarray.
                
            Returns:
                TreeNode: The root of the subtree constructed from the subarray.
            """
            # Base case: If the left pointer exceeds the right pointer, the subarray is empty.
            # This indicates the end of a branch, so we return None.
            if left > right:
                return None
            
            # Find the middle element of the current subarray. This element will be the root
            # of the current subtree to ensure the tree remains height-balanced.
            mid = (left + right) // 2
            
            # Create a new TreeNode with the middle element's value.
            # This node becomes the root of the current subtree.
            node = TreeNode(nums[mid]) 
            
            # Recursively build the left subtree using the left half of the subarray.
            # The range is from `left` to `mid - 1`.
            node.left = convert(left, mid - 1)
            
            # Recursively build the right subtree using the right half of the subarray.
            # The range is from `mid + 1` to `right`.
            node.right = convert(mid + 1, right)
            
            # Return the newly created root of the subtree.
            return node
        
        # Start the recursive conversion process with the entire array.
        # The initial range is from index 0 to the last index of the array.
        return convert(0, len(nums) - 1)
