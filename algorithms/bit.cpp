#include<bits/stdc++.h>
#include<iostream>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
using namespace std;

#define ff              first
#define ss              second
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
#define MAX 20001
 
void c_p_c()
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}

//code starts

int n;
int arr[30002];
int bit[30004];

int query(int ind)
{
    int ans = 0;
    while(ind > 0)
    {
        // cout<<ind;
        ans+=bit[ind];
        ind-=(ind & -ind);
    }
    return ans;
}

void update(int ind)
{
    while(ind <= n)
    {
        // cout<<ind;
        bit[ind]+=1;
        ind+=(ind & -ind);
    }
}

int32_t main()
{
    w(qq)
    {
        cin>>n;
        vector<string> st;
        fi(0,n+1) bit[i] = 0;
        fi(0,n) {string temp; cin>>temp; st.pb(temp); }
        vector<string> ac;
        fi(0,n) { string temp; cin>>temp; ac.pb(temp); }
        map<string,int> m;
        // dbg(ac,0,n);
        int ite=  1;
        // cout<<"fsfs";
        // dbg(st,0,n);
        fi(0,n) 
        {
            // cout<<i<<" "<<n;
            m[ac[i]] = ite++;
            // cout<<"fsfs"
        }
        fi(0,n) arr[i] = m[st[i]];
        // dbg(arr,0,n);
        int inv = n*(n-1)/2;
        fi(0,n)
        {
            int ans = query(arr[i]);
            // cout<<"sfs";
            inv-=ans;
            update(arr[i]);
        }
        cout<<inv<<endl;
    }
}