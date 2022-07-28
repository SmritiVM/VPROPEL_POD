#include <iostream>
#include <vector>
#include <map>
using namespace std;
int main()
{
    int n,m; cin>>n>>m;
    map<string,vector<int>> coins;
    vector<string> insertion_order;
    int i,j;
    for(i = 0; i < n; i++)
    {
        string name; cin>>name;
        insertion_order.push_back(name);
        vector<int> v;
        for(j = 0; j < m; j ++)
        {
            int coin; cin>>coin; 
            v.push_back(coin);
        }
        coins[name] = v;
    }
    
    
    int k; cin>>k;
    for(i = 0; i < k; i++)
    {
        
        string name1,name2; cin>>name1>>name2;
        vector<int> v1 = coins[name1];
        vector<int> v2 = coins[name2];
        v1.swap(v2);
        coins[name1] = v1;
        coins[name2] = v2;
    }
    
    
    vector<int>::iterator v_it;
    i = 0;
    while (i < n)
    {
        string name = insertion_order[i];
        vector<int> v = coins[name];
        cout<<name<<' ';
        for(v_it = v.begin(); v_it < v.end(); v_it++)
            cout<<*v_it<<' ';
        cout<<'\n';
        i++;
    }
}