#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <list>
using namespace std;


class Twitter {
    struct Node
    {
        unordered_set<int> followee;
        list<int> tweet;
    };
    int recent_max, time;
    unordered_map<int, int> tweet_time;
    unordered_map<int, Node> user;
public:
    /** Initialize your data structure here. */
    Twitter() {
        time = 0;
        recent_max = 10;
        user.clear();
    }

    void init_user(int user_id)
    {
        user[user_id].followee.clear();
        user[user_id].tweet.clear();
    }
    
    /** Compose a new tweet. */
    void postTweet(int userId, int tweetId) {
        if (user.find(userId) == user.end())
            init_user(userId);

        // 一个用户的tweet最多只用存10个
        if (user[userId].tweet.size() == recent_max)
            user[userId].tweet.pop_back();
        user[userId].tweet.push_front(tweetId);
        tweet_time[tweetId] = ++time;
    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    vector<int> getNewsFeed(int userId) {
        vector<int> res;
        // 先把自己的post加到res中
        for (auto item : user[userId].tweet) {
            res.push_back(item);
        }
        
        for (int followeeId : user[userId].followee) {
            if (followeeId == userId) continue;    // 自己关注自己，跳过
            vector<int> tmp_res;
            auto iter = user[followeeId].tweet.begin();
            int cnt = 0;
            // 线性归并，把时间靠后的那个tweet依次放到tmp_res中
            while (cnt < res.size() && iter!=user[followeeId].tweet.end()) {
                if (tweet_time[res[cnt]] < tweet_time[*iter]) {
                    tmp_res.push_back(*(iter++));
                } else {
                    tmp_res.push_back(res[cnt++]);
                }
                // 只用归并前10个
                if (tmp_res.size() == recent_max)
                    break;
            }

            while (tmp_res.size() < recent_max && cnt < res.size()) {
                tmp_res.push_back(res[cnt++]);
            }
            while (tmp_res.size() < recent_max && iter != user[followeeId].tweet.end()) {
                tmp_res.push_back(*(iter++));
            }
            res = tmp_res;
        }
        return res;
    }
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    void follow(int followerId, int followeeId) {
        if (user.find(followerId) == user.end())
            init_user(followerId);
        if (user.find(followeeId) == user.end())
            init_user(followeeId);
        user[followerId].followee.insert(followeeId);
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    void unfollow(int followerId, int followeeId) {
        // if (user.find(followerId) == user.end())
        //     return;
        user[followerId].followee.erase(followeeId);
    }
};


/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */

void test1()
{
    Twitter *obj = new Twitter();
    obj->postTweet(1, 5);
    vector<int> res1 = obj->getNewsFeed(1);    // [5]
    obj->follow(1, 2);
    obj->postTweet(2, 6);
    vector<int> res2 = obj->getNewsFeed(1);    // [6, 5]
    obj->unfollow(1, 2);
    vector<int> res3 = obj->getNewsFeed(1);    // [5]
    if (res1 == vector<int>{5} && res2 == vector<int>{6, 5} && res3 == res1)
        cout << "test1 success." << endl;
    else
        cout << "test1 failed." << endl;
}

void test2()
{
    Twitter *obj = new Twitter();
    obj->postTweet(1, 5);
    obj->follow(1,1);
    vector<int> res1 = obj->getNewsFeed(1);    // {5}
    if (res1 == vector<int>{5})
        cout << "test2 success." << endl;
    else
        cout << "test2 failed." << endl;
}

void test3()
{
    Twitter *obj = new Twitter();
    obj->postTweet(1, 5);
    obj->follow(1, 2);
    obj->follow(2, 1);
    vector<int> res1 = obj->getNewsFeed(2);   // {5}
    obj->postTweet(2, 6);
    vector<int> res2 = obj->getNewsFeed(1);    // {6,5}
    vector<int> res3 = obj->getNewsFeed(2);    // {6,5}
    obj->unfollow(2,1);
    vector<int> res4 = obj->getNewsFeed(1);    // {6,5}
    vector<int> res5 = obj->getNewsFeed(2);    // {6}
    obj->unfollow(1,2);
    vector<int> res6 = obj->getNewsFeed(1);    // {5}
    vector<int> res7 = obj->getNewsFeed(2);    // {6}
    if (res1 == vector<int>{5} &&
    res2 == vector<int>{6, 5} &&
    res3 == res2 &&
    res4 == res2 &&
    res5 == vector<int>{6} &&
    res6 == res1 &&
    res7 == res5)
        cout << "test3 success." << endl;
    else
        cout << "test3 failed." << endl;
}

void test4()
{
    Twitter *obj = new Twitter();
    obj->postTweet(1, 6765);
    obj->postTweet(5, 671);
    obj->postTweet(3, 2868);
    obj->postTweet(4, 8148);
    obj->postTweet(4, 386);
    obj->postTweet(3, 6673);
    obj->postTweet(3, 7946);
    obj->postTweet(3, 1445);
    obj->postTweet(4, 4822);
    obj->postTweet(1, 3781);
    obj->postTweet(4, 9038);
    obj->postTweet(1, 9643);
    obj->postTweet(3, 5917);
    obj->postTweet(2, 8847);

    obj->follow(1,3);
    obj->follow(1,4);
    obj->follow(4,2);
    obj->follow(4,1);
    obj->follow(3,2);
    obj->follow(3,5);
    obj->follow(3,1);
    obj->follow(2,3);
    obj->follow(2,1);
    obj->follow(2,5);
    obj->follow(5,1);
    obj->follow(5,2);

    // obj->print_follow();

    vector<int> res1 = obj->getNewsFeed(1);     // 1,3,4
    vector<int> res2 = obj->getNewsFeed(2);
    vector<int> res3 = obj->getNewsFeed(3);
    vector<int> res4 = obj->getNewsFeed(4);
    vector<int> res5 = obj->getNewsFeed(5);

    if (res1 == vector<int>{5917,9643,9038,3781,4822,1445,7946,6673,386,8148} &&
    res2 == vector<int>{8847,5917,9643,3781,1445,7946,6673,2868,671,6765} &&
    res3 == vector<int>{8847,5917,9643,3781,1445,7946,6673,2868,671,6765} &&
    res4 == vector<int>{8847,9643,9038,3781,4822,386,8148,6765} &&
    res5 == vector<int>{8847,9643,3781,671,6765})
        cout << "test4 success." << endl;
    else
        cout << "test4 failed." << endl;
}

void test5()
{
    Twitter *obj = new Twitter();
    obj->postTweet(2,5);
    obj->follow(1,2);
    obj->follow(1,2);
    vector<int> res1 = obj->getNewsFeed(1);  // [5]
    if (res1 == vector<int>{5})
        cout << "test5 success." << endl;
    else
        cout << "test5 failed." << endl;
}

int main()
{
    test1();
    test2();
    test3();
    test4();
    test5();

    return 0;
}
