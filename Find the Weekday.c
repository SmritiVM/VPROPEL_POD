#include <stdio.h>
int main()
{ 
    int n,day,m;
    scanf("%d %d %d",&n,&day,&m);
    char* days[7] = {"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"};
    int diff;
    if(m>n)
       diff = (m-n)%7; 
    else
        diff = 7-(n-m)%7;
    int d = diff+day;
    if (d>=7)
        d-=7;
    if (d<0)
        d=7-d;
    
    printf("%s",days[d]);
    return 0;
}