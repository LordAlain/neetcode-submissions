class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxP = 0, l = 0;
        for (int r = 1; r < prices.size(); r++) {
            if (prices[l] < prices[r]) {
                maxP = max(maxP, prices[r] - prices[l]);
            } else {
                l = r;
            }
        }
        return maxP;
    }
};
