class Solution {
public:
    int smallestDivisor(vector<int>& nums, int threshold) {
        int left = 1;
        int right = *max_element(nums.begin(), nums.end());

        while (left < right) {
            int mid = left + (right - left) / 2;
            int total = getSum(nums, mid);

            if (total <= threshold) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

private:
    int getSum(const vector<int>& nums, int divisor) {
        int sum = 0;
        for (int num : nums) {
            sum += (num + divisor - 1) / divisor;
        }
        return sum;
    }
};
