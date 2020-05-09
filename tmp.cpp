#include <iostream>
#include <vector>
using namespace std;

void* memcpy(void *psrc, void *pdst, size_t ilenth)
{
    if (!psrc || !pdst)
        return nullptr;
    if (psrc == pdst)
        return psrc;

    char *pd = (char *)pdst;
    const char *ps = (char *)psrc;

    if (pdst > psrc) {
        for (int i = ilenth - 1; i >= 0; i--) {
            pd[i] = ps[i];
        }
        return pd;
    } else {
        for (int i = 0; i < ilenth; i++)
            pd[i] = ps[i];
        return pd + (size_t(psrc)-size_t(pdst));
    }

}


// hello world, god bless you <-> you bless god, world hello


vector<string> split(string s, char ch)
{
    size_t pos = s.find(ch);
    size_t start = 0;
    vector<string> words;


    for (size_t pos = 0; pos < s.size(); pos++) {
        if (s[pos] == ' ') {
            words.push_back(s.substr(start, pos - start));
            start = pos + 1;
        }
    }

    words.push_back(s.substr(start, min(pos, s.size() - start)));
    return words;
}

string my_reverse(string s1)
{
    vector<string> words_left, words_right;
    size_t comma_pos = s1.find(',');
    if (comma_pos == string::npos)
        comma_pos = s1.size();

    words_left = split(s1.substr(0, comma_pos), ' ');
    words_right = split(s1.substr(comma_pos + 2), ' ');

    reverse(words_left.begin(), words_left.end());
    reverse(words_right.begin(), words_right.end());

    string res = "";

    for (int i = 0; i < words_right.size() - 1; i++) {
        res += words_right[i] + ' ';
    }
    res += words_right.back();
    res += ", ";

    for (int i = 0; i < words_left.size() - 1; i++) {
        res += words_left[i] + ' ';
    }
    res += words_left.back();

    cout << "res = " << res << endl;
    return res;
}

int main()
{
    string s1 = "Hello world, god bless you";
    string expected_str = "you bless god, world Hello";
    string res = my_reverse(s1);
    if (res == expected_str)
        cout << "success" << endl;
    else
        cout << "failed." << endl;

    char buffer[10] = "123456";

    char *psrc = buffer;
    char *pdst = psrc + 2;
    char *res_a = (char *)memcpy(psrc, pdst, 7);
    printf("res = %s\n", res_a);

    char buffer2[10] = "abcdef";
    char *psrc2 = buffer2;
    char *pdst2 = psrc - 2;
    char *res_b = (char *)memcpy(psrc2, pdst2, 7);
    printf("res = %s\n", res_b);

SYN, i
SYN, j, ACK, i+1
ACK, j+1




}