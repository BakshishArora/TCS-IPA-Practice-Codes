#include<bits/stdc++.h>
#include<conio.h>
using namespace std;

int main()
{
    int n1, n2;
    n1=11;
    n2=15;
    int count=0;
    set<char>s;
    for(int i=n1; i<=n2; i++)
    {
        string a = to_string(i);
        int size= a.length();
        for(char x : a){
        s.insert(x);
        }

        if(s.size()==size)
        count++;
    }
    
    cout<<count<<endl;
    getch();
    return 0;

    
}