class Solution:
    def containsDuplicate(self, nums):
        """
        Checks if a list contains any duplicate elements.

        Args:
            nums (list[int]): A list of numbers.

        Returns:
            bool: True if any value appears at least twice in the list, False otherwise.
        """
        # A set is used to store the numbers that have been seen so far.
        # A set provides O(1) average time complexity for adding and checking for membership,
        # which is much more efficient than a list for this purpose.
        seen = set()

        # Iterate through each number in the input list.
        for num in nums:
            # Check if the current number is already in the 'seen' set.
            if num in seen:
                # If it is, we have found a duplicate, so we can immediately
                # return True.
                return True
            # If the number is not in the set, add it to the set.
            # This marks it as "seen" for future checks.
            seen.add(num)

        # If the loop completes without finding any duplicates, it means
        # every element was unique.
        return False
