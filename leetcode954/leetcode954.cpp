class Solution {
public:
    bool canReorderDoubled(vector<int>& arr) {
         unordered_map<int, int> count;
        for (int x : arr) {
            count[x]++;
        }
        vector<int> keys;
        for (auto& p : count) {
            keys.push_back(p.first);
        }
        sort(keys.begin(), keys.end(), [](int a, int b) {
            return abs(a) < abs(b);
        });
        for (int x : keys) {
            int cx = count[x];
            int c2x = count[2 * x];

            if (cx > c2x) {
                return false;
            }
            count[2 * x] -= cx;
        }
        return true;
    }
};
