#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> result;
        for(int i = 0, j; i < words.size(); i = j) {
            int width = 0;
            // j - i表示空格，这里假定空格至少一个长度，这个loop之后的width已经包含了一个空格
            int space = 1, extra = 0;
            for(j = i; j < words.size() && width + words[j].size() + j - i <= maxWidth; j++) {
                width += words[j].size();
            }

            // 注意这里是[i, j)下面的k没有等到j，所以 除数还要减1
            // 这样也可以处理最后一行，如果j == words.size()， 则space就是1
            if(j - i != 1 && j != words.size()) {
                space = (maxWidth - width) / (j - i - 1);  // 平均每个空格要多长
                extra = (maxWidth - width) % (j - i - 1);  // 没有除净，都放在最左边
            }
            string line(words[i]);
            for(int k = i + 1; k < j; k++) {
                line += string(space, ' ');
                if(extra-- > 0) {
                    line += " ";
                }
                line += words[k];
            }
            
            line += string(maxWidth - line.size(), ' ');
            result.push_back(line);
        }
        return result;
    }
};

void test(string test_name, vector<string>& words, int maxWidth, vector<string>& expected)
{
    vector<string> res = Solution().fullJustify(words, maxWidth);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<string> words1 = {"This", "is", "an", "example", "of", "text", "justification."};
    int maxWidth1 = 16;
    vector<string> expected1 = {
        "This    is    an",
        "example  of text",
        "justification.  "
    };
    test("test1", words1, maxWidth1, expected1);

    vector<string> words2 = {"What","must","be","acknowledgment","shall","be"};
    int maxWidth2 = 16;
    vector<string> expected2 = {
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    };
    test("test2", words2, maxWidth2, expected2);

    vector<string> words3 = {"Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"};
    int maxWidth3 = 20;
    vector<string> expected3 = {
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  "
    };
    test("test3", words3, maxWidth3, expected3);

    return 0;
}
