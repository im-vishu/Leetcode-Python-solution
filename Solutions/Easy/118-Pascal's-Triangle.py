# Source : https://oj.leetcode.com/problems/pascals-triangle/
# Author : Hao Chen
# Date   : 2014-06-18

##################################################################################
#
# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#
#
##################################################################################

class Solution:
    def generate(self, numRows):
        """
        Generates the first numRows of Pascal's triangle.
        """
        pascal_triangle = []
        
        for i in range(numRows):
            # Start each row with 1
            row = [1]
            
            # Calculate the middle elements of the row
            if i > 0:
                prev_row = pascal_triangle[i-1]
                for j in range(len(prev_row) - 1):
                    # The value is the sum of the two numbers directly above it
                    row.append(prev_row[j] + prev_row[j+1])
                # End each row with 1
                row.append(1)
            
            pascal_triangle.append(row)
            
        return pascal_triangle

def print_triangle(pt):
    """
    A helper function to print the Pascal's triangle in a formatted way.
    """
    print "["
    if not pt:
        print "]"
        return

    max_len = len(str(pt[-1])) if pt else 0
    for i, row in enumerate(pt):
        # Calculate padding for alignment
        padding = max_len - len(str(row))
        # Print spaces without a newline
        for _ in range(padding // 2):
            print " ",
        
        print "[",
        
        # Print elements of the row
        for j, num in enumerate(row):
            print str(num),
            if j < len(row) - 1:
                print ",",
        
        print "]",
        if i < len(pt) - 1:
            print ","
        else:
            print ""
    print "]"

def main():
    import sys
    
    num_rows = 5
    if len(sys.argv) > 1:
        try:
            num_rows = int(sys.argv[1])
        except ValueError:
            print "Invalid input. Using default numRows = 5."
            
    # Create an instance of the Solution class to call the method
    solution_instance = Solution()
    triangle = solution_instance.generate(num_rows)
    print_triangle(triangle)

if __name__ == "__main__":
    main()
