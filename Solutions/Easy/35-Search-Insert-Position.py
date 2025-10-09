class Solution:
    def searchInsert(self, nums, target):
        """
        Finds the index of a target value in a sorted array. If the target is not found,
        it returns the index where it would be inserted to maintain the sorted order.

        Args:
            nums (list): A sorted list of integers.
            target (int): The integer to search for or insert.

        Returns:
            int: The index of the target or the insertion point.
        """
        # Initialize two pointers for the binary search: 'start' at the beginning of the list
        # and 'end' at the end.
        start = 0
        end = len(nums) - 1

        # The binary search loop continues as long as the search range is valid.
        while start <= end:
            # Calculate the middle index of the current search range.
            mid = (start + end) // 2

            # Case 1: The target is found at the middle index.
            if nums[mid] == target:
                return mid
            # Case 2: The middle element is less than the target.
            # This means the target must be in the right half of the current range.
            elif nums[mid] < target:
                # We update the 'start' pointer to search in the right half.
                start = mid + 1
            # Case 3: The middle element is greater than the target.
            # This means the target must be in the left half of the current range.
            else:
                # We update the 'end' pointer to search in the left half.
                end = mid - 1
        
        # After the loop, the `start` pointer will be at the correct insertion point.
        # This is because the loop terminates when `start` becomes greater than `end`.
        # The `start` pointer will have moved one position past the last checked element,
        # placing it at the correct index for insertion.
        return start
