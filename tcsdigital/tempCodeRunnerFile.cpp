#include<iostream>
using namespace std;
int main()
{
    int x,n,pow=1;
    cin>>x>>n;
    for(int i=0;i<n;i++)
    pow=pow*x;
    cout<<pow;
    return 0;
}