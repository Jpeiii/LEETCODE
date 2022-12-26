class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        // initialize i = 1 if the vector is not empty or 0 if it is
        int i = !nums.empty();

        // iterates through each element
        for (int n : nums)
        {
            // if the current element greater than previous value [mean is not duplicate and increasing],
            // insert to vector
            if (n > nums[i - 1])
            {
                // increate the index
                nums[i++] = n;
            }
        }
        return i;
    }
};