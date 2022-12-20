class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int buy = 0;
        int sell = 0;
        int maxProfit = 0;
        for (int i = 0; i < prices.size(); i++)
        {
            if (prices[buy] < prices[sell])
            {
                int currentProfit = prices[sell] - prices[buy];
                maxProfit = max(maxProfit, currentProfit);
            }
            else
            {
                buy = sell;
            }
            sell++;
        }
        return maxProfit;
    }
};