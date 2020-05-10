#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int minArray(vector<int>& numbers) {
        int l = 0, r = numbers.size() - 1;
        int mid;
        while (l < r) {
            mid = l + (r - l) / 2;
            // 必然右边有序，mid为右边最小的数
            if (numbers[mid] < numbers[r])
                r = mid;
            // 必然左边有序，且mid是一个很大的数，还有更小的数在mid右边
            else if (numbers[r] < numbers[mid])
                l = mid + 1;
            // 去重
            else
                r--;
        }
        return numbers[l];
    }
};

void test(string test_name, vector<int> numbers, int expected)
{
    int res = Solution().minArray(numbers);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<int> numbers1 = {3,4,5,1,2};
    int expected1 = 1;
    test("test1", numbers1, expected1);

    vector<int> numbers2 = {2,2,2,0,1};
    int expected2 = 0;
    test("test2", numbers2, expected2);

}