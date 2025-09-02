class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        std::unordered_map<int, int> freq;
        int count = 0;
        for (int num : nums) {
            if (freq[k- num] > 0) {
                count++;
                freq[k-num]--;
            } else {
                freq[num]++;
            }
        }
        return count;
    }
};
