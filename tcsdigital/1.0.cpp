#include<bits/stdc++.h>
#include<conio.h>
 using namespace std;

  int solve(int n)
 {
    int ans=0, count=0;
    while(n>0)
    {
        int t=n%10;
        ans=ans+((9-t)*pow(10,count++));
        n=n/10;
    }
    return ans;

 }

 int main()
 {
    int n;
    cin>>n;
    if(n>0 || n< 1000000)
    cout<< solve(n);
    else 
    cout<< "Wrong Input";
    getch();
    return 0;
 }