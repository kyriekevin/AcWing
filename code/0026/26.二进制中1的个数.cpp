class Solution {
public:
    int NumberOf1(int n) {
        int res = 0;
        while (n) {
            res++;
            n -= n & -n;
        }
        return res;
    }
};

