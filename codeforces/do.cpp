#include <bits/stdc++.h>
using namespace std;
vector<vector<int> > arr(101,vector<int>(101));
void print(vector<vector<int> > ans,int n)
{
    for(int i = 0;i<n+1;++i)
    {
        for(int j = 0;j < n+1;++j)
        {
            cout<<ans[i][j];
        }
        cout<<"\n";
    }
}
bool solve(vector<vector<int> >&ans ,int row ,int col ,int n )
{
    if (row == n-1  && col == n)
        return true;
    if (col == n)
    {
        row++;
        col = 0;
    }
    if (ans[row][col] !=-1)
        return solve(ans,row, col+1,n);
  if(row==0||col==0)
  {
      for(int i=9;i>=0;i--)
      {
           ans[row][col] = i;
           if (solve(ans,row, col+1,n))
            return true;
      }
  }
 else{
    int z=arr[row-1][col-1]-(ans[row-1][col]+ans[row][col-1]+ans[row-1][col-1]);
    if(z<0||z>9)
        return false;
    ans[row][col] = z;
    if (solve(ans,row, col+1,n))
        return true;
 }

    ans[row][col]=-1;
    return false;
}

int main() {
 // your code goes here
 ios_base::sync_with_stdio(false);
 cin.tie(NULL);
 cout.tie(NULL);
 int n ;
 cin>>n;
 
 
 vector<vector<int> > ans(n+1,vector<int>(n+1,-1));
 for(int i = 0 ;i<n;++i)
 {
     for(int j = 0;j < n;++j)
     {
         cin>>arr[i][j];
             
     }
     
 }
    solve(ans,0,0,n+1);
    print(ans,n);
 return 0;
}