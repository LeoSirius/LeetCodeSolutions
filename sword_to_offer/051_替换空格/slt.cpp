class Solution{
public:
void ReplaceBlank(char str[], int length)
{
    if (str == nullptr || length <= 0)
        return;

    int len_origin = 0;
    int num_blanks = 0;
    for (int i = 0; str[i]; i++) {
        len_origin++;
        if (str[i] == ' ')
            num_blanks++;
    }
    int len_new = len_origin + 2 * num_blanks;
    if (len_new > length)
        return;

    int idx_origin = len_origin;        // 结尾符号 \0也要搬到后面去，所以索引从len开始
    int idx_new = len_new;
    while (idx_origin >= 0 && idx_new > idx_origin) {
        if (str[idx_origin] == ' ') {
            str[idx_new--] = '0';
            str[idx_new--] = '2';
            str[idx_new--] = '%';
        } else {
            str[idx_new--] = str[idx_origin];
        }
        idx_origin--;
    }
}
}