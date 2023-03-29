#include<bits/stdc++.h>
#include<conio.h>
using namespace std;

bool duplicate(int n)
{
    unordered_map<int,int>mp;
    while(n)
    {
        int t=n%10;
        n/=10;
        if (mp.find(t)!=mp.end())
        {
            return true;

        }
        mp[t]++;
        }
        return false;
}

int main()
{
    int n1, n2;
    int count=0;
    cin>>n1>>n2;
    for(int i=n1; i<=n2; i++)
    {
        if(!duplicate(i))
            count++;

    }
    cout<<count<<endl;
    getch();
    return 0;

}