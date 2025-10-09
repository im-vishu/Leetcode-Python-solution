class Solution:
    def singleNumber(self, nums):
        """
        Finds the single unique number in a list where every other number appears exactly twice.

        This solution leverages the properties of the XOR bitwise operator.

        Args:
            nums (list[int]): A list of integers where one element appears once and all others appear twice.

        Returns:
            int: The unique number that appears only once.
        """
        # Initialize a variable `single` to 0. XORing any number with 0
        # returns the number itself (e.g., 5 ^ 0 = 5).
        single = 0
        
        # Iterate through each number in the list.
        for num in nums:
            # The XOR bitwise operator `^` is used.
            # Key properties of XOR:
            # 1. a ^ a = 0 (XORing a number with itself results in 0).
            # 2. a ^ 0 = a (XORing a number with 0 results in the number itself).
            # 3. XOR is commutative and associative (order doesn't matter).
            # By XORing all numbers in the list, pairs of identical numbers will cancel
            # each other out (e.g., 2 ^ 2 = 0), leaving only the unique number.
            single ^= num
            
        # The final value of `single` will be the unique number.
        return single
