#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 200010;

struct PII {
    int a, b, d;
    PII(int a_val, int b_val, int d_val) : a(a_val), b(b_val), d(d_val) {}
    bool operator<(const PII& other) const { 
        return a > other.a;
    }
};

class SegmentTree {
    vector<long long> tree, lazy;
    int n;

    void pushdown(int node) {
        if (lazy[node]) {
            tree[node*2] += lazy[node];
            tree[node*2+1] += lazy[node];
            lazy[node*2] += lazy[node];
            lazy[node*2+1] += lazy[node];
            lazy[node] = 0;
        }
    }

    void pushup(int node) {
        tree[node] = max(tree[node*2], tree[node*2+1]);
    }

public:
    SegmentTree(int size) : n(size), tree(4*size), lazy(4*size) {}

    void update(int node, int l, int r, int L, int R, int val) {
        if (L <= l && r <= R) {
            tree[node] += val;
            lazy[node] += val;
            return;
        }
        pushdown(node);
        int mid = (l + r) / 2;
        if (L <= mid) update(node*2, l, mid, L, R, val);
        if (R > mid) update(node*2+1, mid+1, r, L, R, val);
        pushup(node);
    }

    long long query(int node, int l, int r, int L, int R) {
        if (L > R) return LLONG_MIN;
        if (L <= l && r <= R) return tree[node];
        pushdown(node);
        int mid = (l + r) / 2;
        long long left_max = L <= mid ? query(node*2, l, mid, L, R) : LLONG_MIN;
        long long right_max = R > mid ? query(node*2+1, mid+1, r, L, R) : LLONG_MIN;
        return max(left_max, right_max);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;
    vector<int> d(n+1), c(n+1), limit(n+1);

    for (int i = 1; i <= n; ++i) {
        cin >> d[i] >> c[i] >> limit[i];
        limit[i] = min(limit[i], m);
    }

    SegmentTree st(n);
    long long ans = 0;
    int v = m;
    priority_queue<PII> pq;

    for (int i = 1; i <= n; ++i) {
        v -= d[i];

        while (v < 0 && !pq.empty()) {
            PII current = pq.top();
            pq.pop();

            int day = current.d;
            int maxv = day <= i-1 ? st.query(1, 1, n, day, i-1) : 0;
            int amount = min(current.b, m - (int)maxv);

            if (amount <= 0) continue;

            int l_add = min(amount, -v);
            v += l_add;
            ans += (long long)l_add * current.a;

            if (day <= i-1) {
                st.update(1, 1, n, day, i-1, l_add);
            }

            if (amount > l_add) {
                pq.emplace(current.a, amount - l_add, day);
            }
        }

        if (v < 0) {
            cout << "-1\n";
            return 0;
        }
        
        if (v > 0) {
            st.update(1, 1, n, i, i, v);
        }

        pq.emplace(c[i], limit[i], i);
    }

    cout << ans << "\n";
    return 0;
}
