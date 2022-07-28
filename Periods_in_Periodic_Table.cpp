#include <iostream>
using namespace std;
#include <map>
#include <string>
int main()
{
    multimap<int,string> periods;
    for (int i = 1; i < 8; i++ )
    {
        string element;
        if(i==1)
        {
            for(int j = 0; j < 2; j++)
            {
                cin>>element;
                periods.insert(pair<int,string>(i,element));
            }
        }
        else
        {
            for(int j = 0; j < 5; j++)
            {
                cin>>element;
                periods.insert(pair<int,string>(i,element));
            }
        }
        
    }
    int n; cin>>n;
    multimap<int,string>::iterator it = periods.begin();
    
    while(it!=periods.end())
    {
        int period = it->first;
        string ele = it->second;
        
        if (period==n)
        {
            cout<<ele<<' ';
                
        }
        it++;
            
    }
}