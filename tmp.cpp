#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

struct Room
{
    Room (double j, double f, double j_per_f)
        :j(j), f(f), j_per_f(j_per_f) {}
    double j, f, j_per_f;
    bool operator < (const Room &other) const
    {
        return j_per_f > other.j_per_f;
    }
};

int main()
{
    int m_f, n_room;
    while (scanf("%d %d", &m_f, &n_room) != EOF && (m_f != -1 && n_room != -1)) {
        vector<Room> rooms;
        for (int i = 0; i < n_room; i++) {
            int j, f;
            scanf("%d %d", &j, &f);
            Room room(j, f, double(j) / f);
            rooms.push_back(room);
        }
        sort(rooms.begin(), rooms.end());
        double res_java = 0;
        for (int i = 0; i < rooms.size() && m_f; i++) {
            if (m_f > rooms[i].f) {
                res_java += rooms[i].j;
                m_f -= rooms[i].f;
            } else {
                res_java += rooms[i].j_per_f * m_f;
                m_f = 0;
            }
        }
        printf("%.3f\n", res_java);
    }
    return 0;
}