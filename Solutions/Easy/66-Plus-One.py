class Solution:
    def plusOne(self, digits):
        """
        Adds one to a number represented as a list of digits.

        This method simulates the process of adding one to a number on paper,
        handling carries from right to left.
        
        Args:
            digits (list[int]): A list of non-negative integers representing the number.
                                For example, [1, 2, 3] represents the number 123.
        
        Returns:
            list[int]: The list of digits after adding one.
        """
        n = len(digits)
        
        # We iterate through the digits from the rightmost (least significant) to the left.
        # This is done using a reverse range `range(n - 1, -1, -1)`.
        for i in range(n - 1, -1, -1):
            # Check if the current digit is less than 9.
            if digits[i] < 9:
                # If it is, we can simply increment it by one.
                # There is no carry-over, so the operation is complete.
                digits[i] += 1
                # We return the modified list immediately.
                return digits
            else:
                # If the current digit is 9, setting it to 0 creates a carry-over.
                digits[i] = 0
        
        # If the loop completes without returning, it means all original digits were 9s
        # (e.g., [9], [9, 9], [9, 9, 9]).
        # All digits have been turned into 0s, and there's a final carry-over.
        # To handle this, we prepend a `1` to the list.
        # For example, [9, 9] becomes [0, 0] in the loop, then `[1] + [0, 0]` becomes `[1, 0, 0]`.
        return [1] + digits
