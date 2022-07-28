#include <iostream>
using namespace std;
#include <string>
#include <map>
int main()
{
    int n,i; cin>>n;
    map<string,string> elements;
    for(i = 0; i < n; i++)
    {
        string ele,symbol;
        cin>>ele>>symbol;
        elements[ele] = symbol;
    }
    int choice; cin>>choice;
    
    
    if (choice==1)
    {
        string search_symbol; cin>>search_symbol; 
        map<string, string>::iterator it = elements.begin();
        int found = 0;
        while(it!=elements.end())
        {
            string ele = it->first;
            string symbol = it->second;
            if (symbol==search_symbol)
            {
                cout<<ele;
                found = 1;
            }
            it++;
            
        }
        if (found == 0)
            cout<<"Not found";
        
    }
       
        
    else
    {
        string search_ele; cin>>search_ele;
        if (elements.count(search_ele))
        {
            cout<<elements[search_ele];
            
        }
        else
            cout<<"Not found";
    }
    return 0;
}