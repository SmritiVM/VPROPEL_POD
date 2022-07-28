#include<iostream>

using namespace std;

#include<vector>

int main()

{
int n_plus_1; cin>>n_plus_1;
vector<float> g1;
vector<float> g2;
int n = n_plus_1 - 1;
for (int i=0;i<n_plus_1;i++)
{
    float element;cin>>element;
    g1.push_back(element);
}
for (int i=0;i<n_plus_1;i++)
{
    float element;cin>>element;
    g2.push_back(element);
}
int error_pos_g1; cin>>error_pos_g1;
int error_pos_g2; cin>>error_pos_g2;

vector<float>::iterator it1 =g1.begin();
g1.erase(it1+error_pos_g1-1);

vector<float>::iterator it2 =g2.begin();
g2.erase(it2+error_pos_g2-1);

for(int i=0;i<g1.size();i++)

{

cout<<g1[i]<<' ';

}
cout<<endl;
for(int i=0;i<g2.size();i++)

{

cout<<g2[i]<<' ';

}
cout<<endl;

if(g1==g2)

cout<<"Equal";

else if((g1[0]-g2[0])==g1[1]-g2[1])
cout<<"Good";
else
cout<<"Bad";

}