#include <iostream>
using namespace std;
int main()
{
    unsigned long long int n,c1,c2;
    cin>>n>>c1>>c2;
    unsigned long long int d = (n*(n-3))/2;
    unsigned long long int adj_total = c1*n;
    unsigned long long int non_adj_total = d*c2;
    unsigned long long int total = c1*n + d*c2;
    cout<<total;
    return 0;
}