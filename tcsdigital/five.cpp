#include<iostream>
#include<conio.h>
usiing namespace std;

int main()
{
    int n,m;
    cin>>n>>m;

    while(n>m)
    {
        for(int i=m; i<=n; i++)
        {
        if(i<100)
        cout<<"0"<<i<<" ";
        }
    }
}