class Solution {
    public int smallestDivisor(int[] nums, int threshold) {
        int left = 1;
        int right = getMax(nums); 
        while (left < right) {
            int mid = (left + right) / 2;
            int total = getSum(nums, mid);
            if (total <= threshold) {
                right = mid; 
            } else {
                left = mid + 1; 
            }
        }
        return left;
    }
    private int getMax(int[] nums) {
        int max = nums[0];
        for (int num : nums) {
            max = Math.max(max, num);
        }
        return max;
    }
    private int getSum(int[] nums, int divisor) {
        int sum = 0;
        for (int num : nums) {
            sum += (num + divisor - 1) / divisor;
        }
        return sum;
}
