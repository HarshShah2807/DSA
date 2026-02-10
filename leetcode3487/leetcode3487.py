class Solution:
    def maxSum(self, nums: List[int]) -> int:
        mx = max(nums)
        if mx <= 0:
            return mx
        seen = set()
        ans = 0
        for x in nums:
            if x > 0 and x not in seen:
                ans += x
                seen.add(x)
        return ans
