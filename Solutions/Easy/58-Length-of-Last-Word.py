class Solution:
    def lengthOfLastWord(self, s):
        """
        Given a string s consisting of alphabets and spaces, return the length of the last word.
        A word is a sequence of non-space characters.

        Args:
            s: The input string.

        Returns:
            The length of the last word, or 0 if no last word exists.
        """
        # First, trim trailing spaces
        s = s.rstrip(' ')

        # If the string is empty after trimming, there are no words
        if not s:
            return 0

        # Find the last space to determine the start of the last word
        last_space_index = s.rfind(' ')

        # If no space is found, the whole string is one word
        if last_space_index == -1:
            return len(s)
        else:
            # The length is the total length minus the index of the last space and the space itself
            return len(s) - 1 - last_space_index
