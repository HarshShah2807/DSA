class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findIndex(isFirst):
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    if isFirst:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index
        first = findIndex(True)
        last = findIndex(False)
        return [first, last]       
