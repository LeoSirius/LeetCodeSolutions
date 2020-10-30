#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string simplifyPath(string path) {
        vector<string> stk;
        size_t pos = 0;
        string token;
        path += '/';       // in order to let while loop handle last dir

        while ((pos = path.find('/')) != string::npos) {
            token = path.substr(0, pos);  // substr before /
            if (token != "") {
                if (token == ".");
                else if (token == "..") {
                    if (!stk.empty()) stk.pop_back();
                } else
                    stk.push_back(token);
            }
            path.erase(0, pos + 1);       // pos没有包括/，这里加1，把'/'也去掉
        }

        string res = "";
        for (string dir : stk)
            res += "/" + dir;
        return res == "" ? "/" : res;
    }
};

void test(string test_name, string path, string expected)
{
    string res = Solution().simplifyPath(path);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string path1 = "/home/";
    string expected1 = "/home";
    test("test1", path1, expected1);

    string path2 = "/../";
    string expected2 = "/";
    test("test2", path2, expected2);

    string path3 = "/home//foo/";
    string expected3 = "/home/foo";
    test("test3", path3, expected3);

    string path4 = "/a/./b/../../c/";
    string expected4 = "/c";
    test("test4", path4, expected4);

    string path5 = "/a/../../b/../c//.//";
    string expected5 = "/c";
    test("test5", path5, expected5);

    string path6 = "/a//b////c/d//././/..";
    string expected6 = "/a/b/c";
    test("test6", path6, expected6);

    return 0;
}