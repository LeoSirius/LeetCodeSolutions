#include<iostream>
#include<queue>
using namespace std;

struct
Status
{
    int s_has, n_has, m_has;    // 三个属性分别表示当前状态下，snm中已有的可乐的体积
    int t;
};
queue<Status> Q;

bool mark[101][101][101];   // 对体积状态进行标记，只有第一次包含的状态有效，因为我们求t的最小值

void
a_to_b (int &a, int a_total, int &b, int b_total)
{
    // 把a杯子中的a体积可乐导入b杯子中
    // 分两种情况：a可全部倒入b中，a不能全部倒入b中
    if (b_total - b >= a) {
        b += a;
        a = 0;
    } else {
        a -= b_total - b;
        b = b_total;
    }
}

int
test_status (int s_has, int n_has, int m_has, int t, int half)
{
    if (mark[s_has][n_has][m_has] == false) {
    cout << "s = " << s_has << ", n = " << n_has << ", m = " << m_has << ", t = " << t << endl;

        mark[s_has][n_has][m_has] = true;
        // 若已经平分，则返回当前次数
        if ((s_has == half && n_has == half) ||
            (n_has == half && m_has == half) ||
            (m_has == half && s_has == half))
            return t + 1;

        Status new_status;
        new_status.s_has = s_has;
        new_status.n_has = n_has;
        new_status.m_has = m_has;
        new_status.t = t + 1;
        Q.push(new_status);
    }
    return 0;       // 返回0 表示当前匹配失败
}

int
BFS (int s, int n, int m)
{
    while (!Q.empty()) {
        Status cur_status = Q.front(); Q.pop();
        int s_has, n_has, m_has;
        int test_t;
        
        // 下面6中情况，分别探测
        // s->n, s->m, n->m, n->s, m->s, m->n
        s_has = cur_status.s_has;
        n_has = cur_status.n_has;
        m_has = cur_status.m_has;
        a_to_b(s_has, s, n_has, n);
        test_t = test_status(s_has, n_has, m_has, cur_status.t, s / 2);
        if (test_t != 0) return test_t;

        s_has = cur_status.s_has;
        n_has = cur_status.n_has;
        m_has = cur_status.m_has;
        a_to_b(s_has, s, m_has, m);
        test_t = test_status(s_has, n_has, m_has, cur_status.t, s / 2);
        if (test_t != 0) return test_t;

        s_has = cur_status.s_has;
        n_has = cur_status.n_has;
        m_has = cur_status.m_has;
        a_to_b(n_has, n, m_has, m);
        test_t = test_status(s_has, n_has, m_has, cur_status.t, s / 2);
        if (test_t != 0) return test_t;

        s_has = cur_status.s_has;
        n_has = cur_status.n_has;
        m_has = cur_status.m_has;
        a_to_b(n_has, n, s_has, s);
        test_t = test_status(s_has, n_has, m_has, cur_status.t, s / 2);
        if (test_t != 0) return test_t;

        s_has = cur_status.s_has;
        n_has = cur_status.n_has;
        m_has = cur_status.m_has;
        a_to_b(m_has, m, n_has, n);
        test_t = test_status(s_has, n_has, m_has, cur_status.t, s / 2);
        if (test_t != 0) return test_t;

        s_has = cur_status.s_has;
        n_has = cur_status.n_has;
        m_has = cur_status.m_has;
        a_to_b(m_has, m, s_has, s);
        test_t = test_status(s_has, n_has, m_has, cur_status.t, s / 2);
        if (test_t != 0) return test_t;
    }
    return 0;       // 返回0，表示整个BFS都没有结果
}

int
main ()
{
    int s, n, m;
    while (scanf("%d %d %d", &s, &n, &m) != EOF && !(s == 0 && n == 0 && m == 0)) {
        if (s % 2 == 1) {
            // 奇数不可能平分，直接pass
            puts("NO");
            continue;
        }
        for (int i = 0; i <= s; i++)
            for (int j = 0; j <= n; j++)
                for (int k = 0; k <= m; k++)
                    mark[i][j][k] = false;
        
        Status init_status;
        init_status.s_has = s;
        init_status.n_has = 0;
        init_status.m_has = 0;
        init_status.t = 0;
        while (!Q.empty()) Q.pop();
        Q.push(init_status);
        mark[s][0][0] = true;
        int res = BFS(s, n, m);
        if (res != 0)
            printf("%d\n", res);
        else
            printf("NO\n");
    }
    return 0;
}
