"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
"""
class Solution:
    # @param n, an integer
    # @return an integer
    #method 1
    def reverseBits(self, n):
        return int(bin(n)[2:].rjust(32, '0')[::-1], 2)
    
    #method 2
    def reverseBits1(self, n):
        res = 0
        for i in range(32):
            last = n & 1
            n >>= 1
            res <<= 1
            res |= last
        return res