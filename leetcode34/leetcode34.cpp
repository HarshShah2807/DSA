vector<int> searchRange(vector<int>& nums, int target) {
    auto lower = findBound(nums, target, true);
    auto upper = findBound(nums, target, false);
    return { lower, upper };
}

int findBound(vector<int>& nums, int target, bool isFirst) {
    int left = 0, right = nums.size() - 1, bound = -1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            bound = mid;
            if (isFirst) right = mid - 1;
            else left = mid + 1;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return bound;
}
