class Solution:
    def specialTriplets(self, nums):
        mod = 10**9 + 7
        left = {}
        right = {}
        for x in nums:
            right[x] = right.get(x, 0) + 1
        ans = 0
        for x in nums:
            right[x] -= 1
            target = x * 2
            left_count = left.get(target, 0)
            right_count = right.get(target, 0)
            ans = (ans + left_count * right_count) % mod
            left[x] = left.get(x, 0) + 1
        return ans
