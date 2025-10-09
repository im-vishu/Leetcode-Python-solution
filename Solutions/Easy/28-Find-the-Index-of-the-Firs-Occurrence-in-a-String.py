class Solution:
    def strStr(self, haystack, needle):
        """
        Implements the strStr() function, which finds the first occurrence 
        of the needle string in the haystack string using a brute-force approach.

        Args:
            haystack (str): The string to be searched.
            needle (str): The substring to search for.

        Returns:
            int: The starting index of the first occurrence of needle in haystack, 
                 or -1 if needle is not part of haystack.
        """
        
        # If needle is empty, return 0 as per typical problem constraints.
        if not needle:
            return 0
        
        N = len(haystack)
        M = len(needle)
        
        # Handle the case where haystack is shorter than needle
        if M > N:
            return -1
        
        # Outer loop iterates through all possible starting indices (i) for the match
        # The loop range goes from i = 0 up to N - M
        for i in range(N - M + 1):
            
            # Inner loop compares the needle with the slice of haystack starting at i
            match_found = True
            for j in range(M):
                # Check characters: haystack[i + j] vs needle[j]
                if haystack[i + j] != needle[j]:
                    match_found = False
                    break
            
            # If the inner loop completed without a mismatch
            if match_found:
                return i
                
        # If the outer loop finishes without a match
        return -1

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        ("sadbutsad", "sad", 0),  # Match at start
        ("leetcode", "leeto", -1), # No match
        ("hello", "ll", 2), # Match in middle
        ("aaaaa", "bba", -1), # No match
        ("abc", "", 0), # Empty needle
        ("", "a", -1), # Empty haystack
        ("mississippi", "issip", 4), # Overlapping match
    ]
    
    print("--- Implement strStr() Test Results ---")
    for haystack, needle, expected in test_cases:
        result = sol.strStr(haystack, needle)
        # Using str.format() for compatibility
        output = "strStr(\"{h}\", \"{n}\") -> Result: {r} (Expected: {e})".format(
            h=haystack, n=needle, r=result, e=expected
        )
        print(output)
