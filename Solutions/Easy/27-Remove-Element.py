class Solution:
    def removeElement(self, nums, val):
        """
        Removes all occurrences of a value from a list in-place and returns the new length.

        Args:
            nums (list): The list of integers.
            val (int): The value to be removed.

        Returns:
            int: The new length of the list after removal.
        """
        # 'pos' is a pointer that tracks the position where the next
        # non-`val` element should be placed. It also represents the new length.
        pos = 0
        
        # We iterate through the list with a second pointer, 'i'.
        for i in range(len(nums)):
            # If the element at the current position 'i' is NOT the value we want to remove...
            if nums[i] != val:
                # ...we move this non-`val` element to the position indicated by 'pos'.
                # This effectively overwrites any `val` elements that we've encountered.
                nums[pos] = nums[i]
                
                # We then increment 'pos' to prepare for the next non-`val` element.
                # All elements before 'pos' are guaranteed to be non-`val` elements.
                pos += 1
                
        # The final value of 'pos' is the new length of the modified list,
        # as it points to the position just after the last non-`val` element.
        return pos
