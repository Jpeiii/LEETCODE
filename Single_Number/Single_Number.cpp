class Solution
{
public:
    int singleNumber(vector<int> &nums)
    {
        unordered_map<int, int> umap;
        for (auto i : nums)
        {
            umap[i]++;
        }
        for (auto i : umap)
        {
            if (i.second == 1)
            {
                return i.first;
            }
        }
        return -1;
    }
};

class Solution
{
public:
    int singleNumber(vector<int> &nums)
    {
        int res = 0;
        for (auto i : nums)
        {
            res = i ^ res;
        }
        return res;
    }
};