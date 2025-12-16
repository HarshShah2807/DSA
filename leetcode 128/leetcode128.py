class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        setnums = set(nums)
        best = 0
        for i in setnums:
            if i - 1 not in setnums:
                length = 1
                while i + length in setnums:
                    length += 1
                best = max(best, length)
        return best
