from typing import *

from collections import defaultdict

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user_map = {}  # user_id -> {'followee': set(), 'tweets':[]}
        self.time = 0
        self.recent_max = 10
        self.tweet_id2time = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.user_map:
            self.user_map[userId] = {'tweets':[], 'followee': set()}

        # 一个用户只需要存10个就行了
        if len(self.user_map[userId]['tweets']) == self.recent_max:
            self.user_map[userId]['tweets'].pop()

        # 越晚出现，时间数越大，越排在前面
        self.user_map[userId]['tweets'].insert(0, tweetId)
        self.tweet_id2time[tweetId] = self.time
        self.time += 1




    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.user_map:
            return []
        res = self.user_map[userId]['tweets']   # 先把自己所有twe存到res中

        for followee_id in self.user_map[userId]['followee']:
            if followee_id == userId: continue  # 自己follow自己，跳过
            tmp_res = []
            p_res, p_cur = 0, 0
            while (p_res < len(res) and
                p_cur < len(self.user_map[followee_id]['tweets']) and
                len(tmp_res) < self.recent_max):
                cur_t_id = self.user_map[followee_id]['tweets'][p_cur]
                if self.tweet_id2time[res[p_res]] < self.tweet_id2time[cur_t_id]:
                    tmp_res.append(cur_t_id)
                    p_cur += 1
                else:
                    tmp_res.append(res[p_res])
                    p_res += 1
            while len(tmp_res) < self.recent_max and p_res < len(res):
                tmp_res.append(res[p_res])
                p_res += 1
            while len(tmp_res) < self.recent_max and p_cur < len(self.user_map[followee_id]['tweets']):
                cur_t_id = self.user_map[followee_id]['tweets'][p_cur]
                tmp_res.append(cur_t_id)
                p_cur += 1
            res = tmp_res
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId == followerId:
            return
        if followerId not in self.user_map:
            self.user_map[followerId] = {'tweets':[], 'followee': set()}
        if followeeId not in self.user_map:
            self.user_map[followeeId] = {'tweets':[], 'followee': set()}
        self.user_map[followerId]['followee'].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId == followerId:
            return
        if followerId not in self.user_map:
            self.user_map[followerId] = {'tweets':[], 'followee': set()}
        if followeeId not in self.user_map:
            self.user_map[followeeId] = {'tweets':[], 'followee': set()}
        if followeeId in self.user_map[followerId]['followee']:
            self.user_map[followerId]['followee'].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

def test1():
    obj = Twitter()
    obj.postTweet(1, 5)        # User 1 posts a new tweet (id = 5).
    res1 = obj.getNewsFeed(1)  # [5]
    obj.follow(1, 2)           # User 1 follow user2
    obj.postTweet(2, 6)        # User 2 posts a new tweet (id = 6).
    res2 = obj.getNewsFeed(1)  # [6, 5], Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    obj.unfollow(1, 2)
    res3 = obj.getNewsFeed(1)  # [5]
    if (res1, res2, res3) == ([5], [6,5], [5]):
        print('test1 success.')
    else:
        print('test1 failed.')

def test2():
    obj = Twitter()
    obj.postTweet(1, 1)
    res1 = obj.getNewsFeed(1)  # [1]
    obj.follow(2, 1)
    res2 = obj.getNewsFeed(2)  # [1]
    obj.unfollow(2,1)
    res3 = obj.getNewsFeed(2)  # []
    if (res1, res2, res3) == ([1], [1], []):
        print('test2 success.')
    else:
        print('test2 failed.')

def test3():
    obj = Twitter()
    res1 = obj.getNewsFeed(1) # []
    if res1 == []:
        print('test3 success.')
    else:
        print('test3 failed.')

def test4():
    obj = Twitter()
    obj.postTweet(1, 5)
    obj.unfollow(1, 1)
    res1 = obj.getNewsFeed(1) # [5]
    if res1 == [5]:
        print('test4 success.')
    else:
        print('test4 failed.')


def test5():
    obj = Twitter()
    obj.postTweet(1, 4)
    obj.postTweet(2, 5)
    obj.unfollow(1, 2)
    res1 = obj.getNewsFeed(1)
    if res1 == [4]:
        print('test5 success.')
    else:
        print('test5 failed.')

def test6():
    obj = Twitter()
    obj.postTweet(2,5)
    obj.postTweet(1,3)
    obj.postTweet(1,101)
    obj.postTweet(2,13)
    obj.postTweet(2,10)
    obj.postTweet(1,2)
    obj.postTweet(2,94)
    obj.postTweet(2,505)
    obj.postTweet(1,333)
    obj.postTweet(1,22)
    res1 = obj.getNewsFeed(2)
    obj.follow(2, 1)
    res2 = obj.getNewsFeed(2)
    if (res1, res2) == ([505,94,10,13,5], [22,333,505,94,2,10,13,101,3,5]):
        print('test6 success.')
    else:
        print('test6 failed.')

def test7():
    o = Twitter()
    o.postTweet(1, 5)
    o.postTweet(1,3)
    o.postTweet(1,101)
    o.postTweet(1,13)
    o.postTweet(1,10)
    o.postTweet(1,2)
    o.postTweet(1,94)
    o.postTweet(1,505)
    o.postTweet(1,333)
    o.postTweet(1,22)
    o.postTweet(1,11)
    res = o.getNewsFeed(1)
    if res == [11,22,333,505,94,2,10,13,101,3]:
        print('test7 success.')
    else:
        print('test7 failed.')


def test8():

    obj = Twitter()
    obj.postTweet(1, 6765)
    obj.postTweet(5, 671)
    obj.postTweet(3, 2868)
    obj.postTweet(4, 8148)
    obj.postTweet(4, 386)
    obj.postTweet(3, 6673)
    obj.postTweet(3, 7946)
    obj.postTweet(3, 1445)
    obj.postTweet(4, 4822)
    obj.postTweet(1, 3781)
    obj.postTweet(4, 9038)
    obj.postTweet(1, 9643)
    obj.postTweet(3, 5917)
    obj.postTweet(2, 8847)

    obj.follow(1,3)
    obj.follow(1,4)
    obj.follow(4,2)
    obj.follow(4,1)
    obj.follow(3,2)
    obj.follow(3,5)
    obj.follow(3,1)
    obj.follow(2,3)
    obj.follow(2,1)
    obj.follow(2,5)
    obj.follow(5,1)
    obj.follow(5,2)


    res1 = obj.getNewsFeed(1)
    res2 = obj.getNewsFeed(2)
    res3 = obj.getNewsFeed(3)
    res4 = obj.getNewsFeed(4)
    res5 = obj.getNewsFeed(5)

    if (res1, res2, res3, res4, res5) == (
        [5917,9643,9038,3781,4822,1445,7946,6673,386,8148],
        [8847,5917,9643,3781,1445,7946,6673,2868,671,6765],
        [8847,5917,9643,3781,1445,7946,6673,2868,671,6765],
        [8847,9643,9038,3781,4822,386,8148,6765],
        [8847,9643,3781,671,6765]
    ):
        print('test8 success.')
    else:
        print('test8 failed.')

def test9():
    o = Twitter()
    o.postTweet(1,5)
    o.postTweet(2,3)
    o.postTweet(1,101)
    o.postTweet(2,13)
    o.postTweet(2,10)
    o.postTweet(1,2)
    o.postTweet(1,94)
    o.postTweet(2,505)
    o.postTweet(1,333)
    o.postTweet(2,22)
    o.postTweet(1,11)
    o.postTweet(1,205)
    o.postTweet(2,203)
    o.postTweet(1,201)
    o.postTweet(2,213)
    o.postTweet(1,200)
    o.postTweet(2,202)
    o.postTweet(1,204)
    o.postTweet(2,208)
    o.postTweet(2,233)
    o.postTweet(1,222)
    o.postTweet(2,211)
    res1 = o.getNewsFeed(1)
    o.follow(1,2)
    res2 = o.getNewsFeed(1)
    o.unfollow(1,2)
    res3 = o.getNewsFeed(1)

    if (res1, res2, res3) == (
        [222,204,200,201,205,11,333,94,2,101],
        [211, 222, 233, 208, 204, 202, 200, 213, 201, 203],
        [222,204,200,201,205,11,333,94,2,101]
    ):
        print('test9 success')
    else:
        print('test9 failed')

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()

# Design a simplified version of Twitter where users can post tweets,
#  follow/unfollow another user and is able to see the 10 most recent
#  tweets in the user's news feed. Your design should support the following methods:

# postTweet(userId, tweetId): Compose a new tweet.
# getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed.
#  Each item in the news feed must be posted by users who the user
#  followed or by the user herself. Tweets must be ordered from most recent
#  to least recent.
# follow(followerId, followeeId): Follower follows a followee.
# unfollow(followerId, followeeId): Follower unfollows a followee.
# Example:

# Twitter twitter = new Twitter()

# // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5)

# // User 1's news feed should return a list with 1 tweet id -> [5].
# twitter.getNewsFeed(1)

# // User 1 follows user 2.
# twitter.follow(1, 2)

# // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6)

# // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# // Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.getNewsFeed(1)

# // User 1 unfollows user 2.
# twitter.unfollow(1, 2)

# // User 1's news feed should return a list with 1 tweet id -> [5],
# // since user 1 is no longer following user 2.
# twitter.getNewsFeed(1)
