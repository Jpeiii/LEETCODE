class Solution
{
public:
    bool containsDuplicate(vector<int> &nums)
    {
        set<int> a;
        for (int i : nums)
        {
            if (a.find(i) != a.end())
            {
                return true;
            }
            a.insert(i);
        }
        return false;
    }
};