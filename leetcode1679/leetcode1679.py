class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c=Counter(nums)
        count=0
        for i in nums:
            if c[k-i] >0 and c[i]>0:
                if i == k - i and c[i] < 2:
                    continue
                count+=1
                c[k-i]-=1
                c[i]-=1
            
        return count
