class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = Counter(nums)
        nums = sorted(points)

        take = skip = 0
        prev = None

        for num in nums:
            curr_points = num * points[num]

            if prev is not None and num == prev + 1:
                take, skip = skip + curr_points, max(skip, take)
            else:
                take, skip = max(take, skip) + curr_points, max(take, skip)

            prev = num

        return max(take, skip)
        
