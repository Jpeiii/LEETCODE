class Solution
{
public:
    vector<int> topKFrequent(vector<int> &nums, int k)
    {
        unordered_map<int, int> hashmap;
        vector<vector<int>> frequency(nums.size() + 1);
        for (int n : nums)
        {
            hashmap[n]++;
        }

        for (auto &[key, value] : hashmap)
        {
            frequency[value].push_back(key);
        }

        vector<int> result;
        for (int i = nums.size(); i > 0; i--)
        {
            for (int n : frequency[i])
            {
                result.push_back(n);
                if (result.size() == k)
                {
                    return result;
                }
            }
        }
        return result;
    }
};