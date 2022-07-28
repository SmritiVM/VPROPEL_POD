#include<iostream>

using namespace std;

#include<string>
#include <vector>

int main()

{
int n,i; cin>>n;
string array_s[n];
for (i=0;i<n;i++)
{
    cin>>array_s[i];
}
string w; cin>>w;


int max_strength = 0;
std::vector<std::string> word;

for (i=0;i<n;i++)
{
    int j,l,pos;
    l = array_s[i].length();
    int strength = 0;
    for (j=0;j<l;j++)
    {
        pos = w.find(array_s[i][j]);
        if (pos!=-1)
        {
            strength += j*pos;
        }
    }
    if (strength > max_strength)
    {
        max_strength = strength;
        word.erase(word.begin(),word.end());
        word.push_back(array_s[i]);
    }
    else if (strength == max_strength)
    {
        word.push_back(array_s[i]);
    }
}

for(i=0;i<word.size();i++)
{
    cout<<word[i]<<endl;
}

return 0;
}
