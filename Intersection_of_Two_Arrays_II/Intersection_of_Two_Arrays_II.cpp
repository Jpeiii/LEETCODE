class Solution
{
public:
    vector<int> intersect(vector<int> &nums1, vector<int> &nums2)
    {
        unordered_map<int, int> h1;
        unordered_map<int, int> h2;

        for (int x : nums1)
        {
            h1[x]++;
        }

        for (int x : nums2)
        {
            h2[x]++;
        }
        vector<int> result;
        for (auto i : h1)
        {
            if (h2.find(i.first) != h2.end())
            {

                int frequent;
                frequent = min(h2.at(i.first), i.second);
                for (int j = 0; j < frequent; j++)
                {
                    result.push_back(i.first);
                }
            }
        }
        return result;
    }
};