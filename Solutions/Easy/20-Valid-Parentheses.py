class Solution:
    def isValid(self, s):
        """
        Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid using a stack-based approach.

        The brackets must close in the correct order.

        Args:
            s (str): The input string.

        Returns:
            bool: True if the string is valid, False otherwise.
        """
        
        # Use a list as a stack.
        stack = []
        
        # Define a mapping for matching opening and closing brackets.
        # This makes the code cleaner than a series of if/else if checks.
        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        # Iterate over each character in the string
        for char in s:
            
            # If the character is a closing bracket
            if char in mapping:
                
                # Pop the top element from the stack. If the stack is empty, 
                # assign a dummy value that won't match any opening bracket.
                # This prevents an IndexError on an empty stack.
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped opening bracket matches the current closing bracket
                if mapping[char] != top_element:
                    return False
            
            # If the character is an opening bracket
            elif char in mapping.values():
                stack.append(char)
            
            # If the character is not a bracket, treat it as invalid 
            else:
                return False

        # After iterating through the whole string, the stack must be empty
        # for the string to be valid (all opening brackets were closed).
        return not stack

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("{{{", False),
        ("{123}", False) # Tests the "return false" for non-bracket characters
    ]
    
    print("--- Valid Parentheses Test Results ---")
    for s, expected in test_cases:
        result = sol.isValid(s)
        # Using str.format() for compatibility
        output = "isValid(\"{s}\") -> Result: {r} (Expected: {e})".format(
            s=s, r=result, e=expected
        )
        print(output)
