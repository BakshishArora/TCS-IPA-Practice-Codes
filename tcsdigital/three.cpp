#include<bits/stdc++.h>
#include<conio.h>
using namespace std;

int main()
{
    string arr[]={"goto", "break", "defer", "map", "func"};
    string c;
    int cn=0;

  cin>>c;

    for(int i=0; i<5;i++)
    {
        if(c==arr[i]){
        cn=1;
        break;
        }
    }
    if(cn==1)
    cout<<c<<" is a keyword";
    else
    cout<<c<<" is not a keyword";

    getch();
    return 0;
}