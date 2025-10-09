class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Merges two sorted arrays, nums1 and nums2, into nums1 in-place.

        Args:
            nums1 (list[int]): The first array with a length of m + n.
            m (int): The number of elements in nums1 that need to be merged.
            nums2 (list[int]): The second array with a length of n.
            n (int): The number of elements in nums2.
        
        Returns:
            None: The function modifies nums1 in-place.
        """
        # `ia` points to the last element of the initialized part of `nums1`.
        ia = m - 1
        # `ib` points to the last element of `nums2`.
        ib = n - 1
        # `i` points to the last position of the combined array in `nums1`.
        # This is where we will place the largest element at each step.
        i = m + n - 1

        # The loop continues as long as there are elements left in `nums2` to process.
        while ib >= 0:
            # Check if there are still elements in `nums1` to consider and if the
            # current element in `nums1` is greater than the one in `nums2`.
            if ia >= 0 and nums1[ia] > nums2[ib]:
                # If `nums1[ia]` is larger, it's the next largest element to be placed.
                # We move it to the current position `i` in the merged array.
                nums1[i] = nums1[ia]
                # Then, we move the `ia` pointer back to consider the next element.
                ia -= 1
            else:
                # If `nums2[ib]` is larger (or if `nums1` is exhausted), it's the next
                # largest element.
                # We move it to the current position `i`.
                nums1[i] = nums2[ib]
                # We move the `ib` pointer back.
                ib -= 1
            
            # In either case, we move the `i` pointer back to the next position for the
            # merged array.
            i -= 1
