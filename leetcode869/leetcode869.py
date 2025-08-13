//https://leetcode.com/problems/reordered-power-of-2/description/

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count=self.counter(n)
        for i in range(30):
            if self.counter(1<<i)==count:
                return True
        return False
    def counter(self,n):
        count=0
        while n>0:
            count+=math.pow(10,n%10)
            n//=10
        return count
