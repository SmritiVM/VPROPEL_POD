#include <iostream>
#include <list>
using namespace std;
class ball
{
    public:
    int radius;
    string colour;
    
    bool operator <(ball b)
    {
        if (radius == b.radius)
            return colour < b.colour;
        else
            return radius < b.radius;
    }
    
    bool operator > (ball b)
    {
        if (radius == b.radius)
            return colour > b.colour;
        else
            return radius > b.radius;
    }
};
int main()
{
    list<ball>l;
    int n; cin>>n;
    list<ball>::iterator it=l.begin();
    for(int i = 0; i < n; i++)
    {
        ball b;
        cin>>b.radius>>b.colour;
        //cout<<b.radius<<b.colour;
        l.insert(it,b);
        it++;
        
    }
    
    l.sort();
    it=l.begin();
    //cout<<l.size();
    int i; cin>>i;
    int ind=1;
    while (it!=l.end())
    {
        //cout<<i<<endl;i++;
        if (ind==i)
        { 
            ball b = *it;
            cout<<b.radius<<" "<<b.colour<<endl;
        }
        ind++;
        it++;
    }
}