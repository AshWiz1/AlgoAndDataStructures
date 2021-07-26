#include<bits/stdc++.h>
#include<iostream>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
using namespace std;

#define endl             "\n"
#define fff             first
#define sss             second
#define int             long long
#define pb              push_back
#define mp              make_pair
#define pii             pair<int,int>
#define vi              vector<int>
#define mii             map<int,int>
#define pqb             priority_queue<int>
#define pqs             priority_queue<int,vi,greater<int> >
#define setbits(x)      __builtin_popcountll(x)
#define zrobits(x)      __builtin_ctzll(x)
#define mod             1000000007
#define inf             1e18
#define ps(x,y)         fixed<<setprecision(y)<<x
#define mk(arr,n,type)  type *arr=new type[n];
#define w(x)            int x; cin>>x; while(x--)
#define fi(x,n)         for(int i=x;i<n;i++)
mt19937                 rng(chrono::steady_clock::now().time_since_epoch().count());
 
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds;
#define n_l '\n'
#define dbg(...) cout << "[" << #__VA_ARGS__ << "]: "; cout << to_string(__VA_ARGS__) << endl
template <typename T, size_t N> long long SIZE(const T (&t)[N]){ return N; } template<typename T> long long SIZE(const T &t){ return t.size(); } string to_string(const string s, long long x1=0, long long x2=1e9){ return '"' + ((x1 < s.size()) ? s.substr(x1, x2-x1+1) : "") + '"'; } string to_string(const char* s) { return to_string((string) s); } string to_string(const bool b) { return (b ? "true" : "false"); } string to_string(const char c){ return string({c}); } template<size_t N> string to_string(const bitset<N> &b, long long x1=0, long long x2=1e9){ string t = ""; for(long long __iii__ = min(x1,SIZE(b)),  __jjj__ = min(x2, SIZE(b)-1); __iii__ <= __jjj__; ++__iii__){ t += b[__iii__] + '0'; } return '"' + t + '"'; } template <typename A, typename... C> string to_string(const A (&v), long long x1=0, long long x2=1e9, C... coords); long long l_v_l_v_l = 0, t_a_b_s = 0; template <typename A, typename B> string to_string(const pair<A, B> &p) { l_v_l_v_l++; string res = "(" + to_string(p.first) + ", " + to_string(p.second) + ")"; l_v_l_v_l--; return res; } template <typename A, typename... C> string to_string(const A (&v), long long x1, long long x2, C... coords) { long long rnk = rank<A>::value; string tab(t_a_b_s, ' '); string res = ""; bool first = true; if(l_v_l_v_l == 0) res += n_l; res += tab + "["; x1 = min(x1, SIZE(v)), x2 = min(x2, SIZE(v)); auto l = begin(v); advance(l, x1); auto r = l; advance(r, (x2-x1) + (x2 < SIZE(v))); for (auto e = l; e != r; e = next(e)) { if (!first) { res += ", "; } first = false; l_v_l_v_l++; if(e != l){ if(rnk > 1) { res += n_l; t_a_b_s = l_v_l_v_l; }; } else{ t_a_b_s = 0; } res += to_string(*e, coords...); l_v_l_v_l--; } res += "]"; if(l_v_l_v_l == 0) res += n_l; return res; } void dbgm(){;} template<typename Heads, typename... Tails> void dbgm(Heads H, Tails... T){ cout << to_string(H) << " | "; dbgm(T...); } 
#define dbgm(...) cout << "[" << #__VA_ARGS__ << "]: "; dbgm(__VA_ARGS__); cout << endl
#define MOD 1000000007
#define MAX 100001
 
void c_p_c()
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
// #ifndef ONLINE_JUDGE
//     freopen("input.txt", "r", stdin);
//     freopen("output.txt", "w", stdout);
// #endif
}



vi g[100001];
vi tg[100001];
int n,k,ans,m;
int arr[100001];
bool vis[100001];
vi com[100001];
stack<int> sta;
int scc=0;

void dfs(int cur)
{
    vis[cur] = true;
    for(int child : g[cur])
    {
        if(!vis[child]) dfs(child);
    }
    sta.push(cur);
}

void dfs1(int cur)
{
    com[scc].pb(arr[cur]);
    vis[cur] =true;
    for(int child : tg[cur])
    {
        if(!vis[child]) dfs1(child);
    }
}

int32_t main()
{   
    cin>>n;
    fi(1,n+1) cin>>arr[i];
    cin>>m;
    fi(0,m)
    {
        int a,b;
        cin>>a>>b;
        g[a].pb(b);
        tg[b].pb(a);
    }
    fi(1,n+1)
    {
        if(!vis[i])
            dfs(i);
    }
    fi(0,n+1) vis[i] = false;
    // dbg(g)
    while(!sta.empty())
    {
        int cur = sta.top();
        sta.pop();
        // cout<<cur<<endl;
        if(!vis[cur])
        {
            // cout<<cur<<endl;
            dfs1(cur);
            scc+=1;
        }
    }
    // cout<<scc;
    int ans = 0;
    int no = 1;
    fi(0,scc)
    {
        int m = *min_element(com[i].begin(),com[i].end());
        // cout<<m<<endl;
        ans+=m;
        int cnt = 0;
        for(int child : com[i]) if(child == m) cnt+=1;
        no=  no*cnt%MOD;
    }
    cout<<ans<<" "<<no<<endl;
}