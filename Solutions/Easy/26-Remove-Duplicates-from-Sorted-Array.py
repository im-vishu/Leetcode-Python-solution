class Solution:
    def removeDuplicates(self, nums):
        """
        Removes duplicates from a sorted list in-place.

        Args:
            nums (list): A list of sorted integers with duplicates.

        Returns:
            int: The new length of the list after removing duplicates.
        """
        # If the input list is empty, there are no elements to process.
        if not nums:
            return 0
        
        # 'len_' is a pointer that tracks the position of the last unique element found so far.
        # It represents the number of unique elements found, and its final value
        # will be the new length of the modified list.
        len_ = 0
        
        # We start iterating from the second element (index 1).
        # We compare each element `nums[i]` with the last unique element we've placed, `nums[len_]`.
        for i in range(1, len(nums)):
            # If the current element `nums[i]` is different from the last unique element `nums[len_]`,
            # it means we've found a new unique element.
            if nums[i] != nums[len_]:
                # We move the `len_` pointer forward to the next available position.
                len_ += 1
                # We then place the new unique element `nums[i]` at this new position.
                # This overwrites the duplicate element that was previously at `nums[len_]`.
                nums[len_] = nums[i]
                
        # After the loop, `len_` holds the index of the last unique element.
        # The number of unique elements is `len_` plus one (for the element at index 0).
        # We return `len_ + 1` as the new length of the list without duplicates.
        return len_ + 1
