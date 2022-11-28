class Solution:
    def isHappy(self, n: int) -> bool:
        val = n
        count = 1
        while val is not 1 and count < 9000:
            val = 0
            if val == 1:
                return True
            
            while n is not 0:
                x = n%10
                val += x * x
                n //= 10
            count+=1
            n = val
        if val == 1:
            return True
        return False