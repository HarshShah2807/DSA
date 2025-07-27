class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(1, n - 1):
            if nums[i] == nums[i - 1]:
                continue
            prev = i - 1
            while prev >= 0 and nums[prev] == nums[i]:
                prev -= 1
            next = i + 1
            while next < n and nums[next] == nums[i]:
                next += 1
            if prev >= 0 and next < n:
                if nums[i] > nums[prev] and nums[i] > nums[next]:
                    count += 1
                elif nums[i] < nums[prev] and nums[i] < nums[next]:
                    count += 1
        return count
