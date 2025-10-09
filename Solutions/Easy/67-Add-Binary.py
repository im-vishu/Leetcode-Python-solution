class Solution:
    def addBinary(self, a, b):
        """
        Adds two binary strings (a and b) and returns their sum as a binary string.

        This function simulates binary addition, processing digits from right to left.

        Args:
            a (str): The first binary string.
            b (str): The second binary string.

        Returns:
            str: The sum of a and b in binary format.
        """
        # `result` will store the final binary sum. It's built in reverse.
        result = ""
        # `i` and `j` are pointers to the current last digits of strings `a` and `b`.
        # They start at the end of the strings to process from right to left.
        i, j = len(a) - 1, len(b) - 1
        # `carry` stores the carry-over value from the previous addition (0 or 1).
        carry = 0

        # The loop continues as long as there are digits in either string to process
        # or there is a remaining carry from the last addition.
        while i >= 0 or j >= 0 or carry:
            # Get the integer value of the current bit from string `a`.
            # If `i` has gone past the beginning of `a`, `bit_a` is 0.
            bit_a = int(a[i]) if i >= 0 else 0
            
            # Get the integer value of the current bit from string `b`.
            # If `j` has gone past the beginning of `b`, `bit_b` is 0.
            bit_b = int(b[j]) if j >= 0 else 0
            
            # Calculate the sum for the current column, including the carry from the previous column.
            current_sum = bit_a + bit_b + carry
            
            # The current digit of the result is the remainder of the `current_sum` when divided by 2.
            # This will be either 0 or 1.
            # We prepend it to the `result` string because we are processing from right to left.
            result = str(current_sum % 2) + result
            
            # The new `carry` is the integer quotient of `current_sum` divided by 2.
            # `1+1=10` in binary, so the sum is 0 and the carry is 1.
            carry = current_sum // 2
            
            # Move the pointers to the next digits to the left.
            i -= 1
            j -= 1
            
        # After the loop, the `result` string contains the final binary sum.
        return result
