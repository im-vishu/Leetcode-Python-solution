class Solution:
    def isPalindrome(self, s):
        """
        Determines if a given string is a palindrome, considering only 
        alphanumeric characters and ignoring case.

        This implementation uses the two-pointer approach, skipping 
        non-alphanumeric characters.

        Args:
            s (str): The input string.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        
        N = len(s)
        i, j = 0, N - 1
        
        # Two-pointer approach: move inwards from both ends
        while i < j:
            
            # Move the left pointer (i) until it hits an alphanumeric character
            # isalnum() checks if a character is alphanumeric (a-z, A-Z, 0-9)
            while i < j and not s[i].isalnum():
                i += 1
            
            # Move the right pointer (j) until it hits an alphanumeric character
            while i < j and not s[j].isalnum():
                j -= 1
            
            # At this point, s[i] and s[j] are alphanumeric (or i >= j)
            
            if i < j:
                # Compare the characters after converting them to lower case
                if s[i].lower() != s[j].lower():
                    return False
                
                # Move both pointers inward for the next comparison
                i += 1
                j -= 1 

        # If the loop completes without returning False, it's a valid palindrome
        return True

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),  # Empty string/string with only spaces is a valid palindrome
        ("0P", False),
        ("Madam", True),
        ("Live on no evil", True)
    ]
    
    print("--- Valid Palindrome Test Results ---")
    for s, expected in test_cases:
        result = sol.isPalindrome(s)
        # Using str.format() for compatibility
        output = "isPalindrome(\"{s}\") -> Result: {r} (Expected: {e})".format(
            s=s, r=result, e=expected
        )
        print(output)
