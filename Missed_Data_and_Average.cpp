#include<iostream>

using namespace std;

#include<vector>
#include <iomanip>

int main()

{

vector<int> v;
int input; cin>>input;
while (input!=-1)
{
    v.push_back(input);
    cin>>input;
}


vector<int>::iterator ptr;

int missed_pos, missed_element;
cin>>missed_pos>>missed_element;
v.insert(v.begin()+missed_pos-1,missed_element);

for(ptr = v.begin();ptr < v.end();ptr++)

{

cout<<*ptr<<"\t";

}
cout<<'\n';
for(int index = 0;index < v.size()-2; index++)
{
  double avg = (v[index]+v[index+1]+v[index+2])/3.0;
  cout<<fixed<<setprecision(2)<<avg<<'\t';
}
}