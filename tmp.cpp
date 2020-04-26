#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, d;
    while (cin >> n >> d) {
        vector<int> pos;
        for (int i = 0; i < n; ++i) {
            int tmp;
            cin >> tmp;
            pos.push_back(tmp);
        }
        int res = 0;
        for (int i = 0; i < n - 2; ++i) {
            for (int j = i + 1; j < n - 1; ++j) {
                for (int k = j + 1; k < n; ++k) {
                    if ((pos[k] - pos[i]) <= d) {
                        ++res;
                    } else {
                        break;
                    }
                }
            }
        }
        cout << res << endl;
    }
    return 0;
}