#include<bits/stdc++.h>
#include<conio.h>
using namespace std;

int main()
{
    int a[]={10,20,30,40,50};
    int k=2;
    int n=5;

    for(int i=0; i<(n-k);i++)
    swap(a[i],a[n-k-1+i]);
    

    for(int i=k; i<n; i++)
    a[i]=a[n-i];

    for(int i=n; i>0; i--)
    cout<<a[i]<<" ";

    getch();
    return 0;
}