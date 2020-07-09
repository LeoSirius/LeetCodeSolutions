### 思路1 记录每个tweid的时间。get的时候按时间归并

struct Node
{
    unordered_set<int> followee;
    list<int> tweet;
};
int recent_max, time;
unordered_map<int, int> tweet_time;
unordered_map<int, Node> user;

关键是设计好数据结构。最后在getNewsFeed时，根据tweet_time找到时间进行线性归并

userId  ->   Node {
    followee set
    tweet list
}
