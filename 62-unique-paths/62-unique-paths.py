class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        import math
        return int(math.comb(m+n-2,n-1))
    
        """
        return int(math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1)))
        """