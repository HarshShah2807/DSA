class Solution {
public:
    bool reorderedPowerOf2(int n) {
        int count = counter(n);
        for (int i = 0; i < 30; ++i) {
            if (counter(1 << i) == count)
                return true;
        }
        return false;
    }
private:
    int counter(int n) {
        int count = 0;
        while (n > 0) {
            count += pow(10, n%10);
            n /= 10;
        }
        return count;
    }
};
