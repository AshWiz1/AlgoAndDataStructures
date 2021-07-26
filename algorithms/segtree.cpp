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

int n;
int t[4*MAX+1]; int  arr[MAX];
int query(   int pos,    int qs,  int qe,    int ss , int se)
{
    if(qs > se or qe < ss)
    {
        return 0;
    }
    if(qs <= ss && se <= qe)
    {
        return t[pos];
    }
    int mid = (ss+se)/2;
    return query(pos*2+1,qs,qe,ss,mid)+ query(pos*2+2,qs,qe,mid+1,se);
    
}

void update(int pos,int l,int r,int indl, int indr)
{
    // cout<<l<<" "<<r<<endl;
    if(t[pos] == l-r+1)
    {
        return;
    }
    if(r < indl || l > indr)
    {
        return;
    }
    if(l == r)
    {
        arr[l] = (int)sqrt(arr[l]);
        t[pos] = arr[l];
        return;
    }
    int mid  = (l+r)/2;
    update (2*pos+1,l,mid,indl,indr);
    update(2*pos+2,mid+1,r,indl,indr);
    t[pos] = t[2*pos+1]+t[2*pos+2];
}

void build(int pos,int l,int r)
{
    if(l == r)
    {
        t[pos] = arr[l];
        return;
    }
    int mid = (l+r)/2;
    build(pos*2+1,l,mid);
    build(pos*2+2,mid+1,r);
    t[pos] = t[2*pos+1]+t[2*pos+2];
}

int32_t main()
{
    // c_p_c();
    int ite=0;
    // c_p_c();
     while(scanf("%lld", &n) != EOF)
     {
        //  fi(0,4*n+1) t[i] = 0;
         fi(0,n) scanf("%lld",&arr[i]);
         build(0,0,n-1);
         printf("Case #%lld:\n",++ite);
         w(qq)
         {
            int x,l,r;
            scanf("%lld %lld %lld",&x,&l,&r);
            if(l>r) swap(l,r);
            if(x==0)
            {
                // dbg(t,0,4*n);
                update(0,0,n-1,l-1,r-1);
                // dbg(t,0,4*n);
            }
            else
            {
                int ans  = query(0,l-1,r-1,0,n-1);
                printf("%lld\n",ans);
            }
            
         }
         printf("\n");
     }
     return 0;
}
