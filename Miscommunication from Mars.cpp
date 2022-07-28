#include <iostream>
using namespace std;
int main()
{
    int n,d,Xor,i,j,n1,n2;
    cin>>n;
    int set[n];
    for(i=0;i<n;i++)
        cin>>set[i];
    cin>>d>>Xor;
    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            
            
            if(((set[j]-set[i]==d)||(set[i]-set[j]==d))&&((set[i]^set[j])==Xor))
            {
                n1 = set[i];
                n2 = set[j];
                break;
            }
        }
    }
    if(n1>n2)
            {

                int temp = n1;
                n1=n2;
                n2=temp;
            }
    cout<<n1<<'\t'<<n2;

    return 0;
}