#1
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

#2
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        count = 0
        for num in list(freq):
            target = k - num
            if target in freq:
                if num == target:
                    count += freq[num] // 2
                else:
                    pairs = min(freq[num], freq[target])
                    count += pairs
                    freq[target] = 0  
                freq[num] = 0  
        return count

#3
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        
        while left < right:
            s = nums[left] + nums[right]
            if s == k:
                count += 1
                left += 1
                right -= 1
            elif s < k:
                left += 1
            else:
                right -= 1
                
        return count
