"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        stack = [[1]*(i+1) for i in range(numRows)]
        for i in range(2, numRows):
            j = 1
            while j < i:
                stack[i][j] = stack[i-1][j-1] + stack[i-1][j]
                j += 1
        return stack