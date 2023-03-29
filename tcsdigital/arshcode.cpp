#include<bits/stdc++.h>
#include<conio.h>
using namespace std;



int main() {
    vector <int> a = {10,20, 30, 40, 50};
    
    int k = 2;
    int n = a.size();
    
    reverse(a.begin(), a.begin() + n - k);
    reverse(a.begin() + n - k, a.end());
    reverse(a.begin(), a.end());
    
    for(auto i : a) cout << i << " ";

    getch();
    return 0;
}