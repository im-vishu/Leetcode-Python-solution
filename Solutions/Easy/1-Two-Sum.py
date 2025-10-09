#
# Given an array of integers, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target,
# where index1 must be less than index2.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=0, index2=1
#
##################################################################################

class Solution:
    def twoSum(self, numbers, target):
        """
        Finds two numbers in a list that add up to a specific target.

        Args:
            numbers (list[int]): A list of integers.
            target (int): The target sum.

        Returns:
            list[int]: A list containing the zero-based indices of the two numbers.
        """
        # A hash map (dictionary in Python) to store numbers and their indices.
        # This allows for O(1) average-time complexity lookup.
        # Key: number, Value: index
        num_map = {}
        
        # Iterate through the list of numbers using enumerate to get both
        # the index (i) and the value (num) at each step.
        for i, num in enumerate(numbers):
            # Calculate the required complement to reach the target sum.
            # If `num` + `complement` = `target`, then `complement` = `target` - `num`.
            complement = target - num
            
            # Check if the required complement already exists as a key in our map.
            # This means we've found the second number in the pair.
            if complement in num_map:
                # If it does, we've found the two numbers.
                # Return the index of the complement (stored in the map) and the
                # index of the current number (i).
                # The problem expects zero-based indices.
                return [num_map[complement], i]
            
            # If the complement is not found, it means the current number is the
            # first number of a potential pair. We store this number and its index
            # in the map for future lookups.
            num_map[num] = i
        
        # Based on the problem assumption that "each input would have exactly one solution",
        # this part of the code should not be reached. It's included for completeness.
        return []

# A main function for demonstration and testing.
def main():
    s = Solution()
    
    # Example from the problem description
    numbers1 = [2, 7, 11, 15]
    target1 = 9
    print("Input: numbers={0}, target={1}".format(numbers1, target1))
    result1 = s.twoSum(numbers1, target1)
    print("Output:", result1)
    
    print("-" * 20)
    
    # Another example
    numbers2 = [3, 2, 4]
    target2 = 6
    print("Input: numbers={0}, target={1}".format(numbers2, target2))
    result2 = s.twoSum(numbers2, target2)
    print("Output:", result2)

if __name__ == "__main__":
    main()
