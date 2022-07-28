#include <iostream>
using namespace std;
#include <vector>
int main()
{
    int n,i; cin>>n;
    vector<char>colours1,colours2;
    for(i = 0; i < n; i++)
    {
        char ele; cin>>ele;
        colours1.push_back(ele);
        colours2.push_back(ele);
    }
    
    int n1; cin>>n1;
    vector<int>p1,p2;
    for(i = 0; i< n1; i++)
    {
        int num; cin>>num;
        p1.push_back(num);
    }
    for(i = 0; i< n1; i++)
    {
        int num; cin>>num;
        p2.push_back(num);
    }
    vector<char>::iterator it1 =colours1.begin();
    vector<char>::iterator it2 =colours2.begin();
    for(i=0;i<n1;i++)
    {
        if (p1[i]==1)
            colours1.assign(it1,it2);
        else if (p1[i]==2)
        {   char r = 'r';
            colours1.insert(colours1.begin()+1,r);}
        else if (p1[i]==3)
            {for (int j=2;j<6;j++)
                {   char r = 'r';
                    colours1.insert(colours1.begin()+j,r);}}
        else if (p1[i]==4)
            colours1.erase(colours1.begin()+3);
        else if (p1[i]==5)
            colours1.erase(colours1.begin()+4,colours1.begin()+5);
        else if (p1[i]==6)
            colours1.erase(colours1.begin(),colours1.begin()+n-1);
        for(i=0;i<n1;i++)
        {
        cout<<colours1[i]<<' ';
        }
        cout<<endl;
    }
    for(i=0;i<n1;i++)
    {
        cout<<colours1[i]<<' ';
    }
}