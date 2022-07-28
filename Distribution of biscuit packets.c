#include <stdio.h>
#include <math.h>
int main()
{
    int m,n,x;
    scanf("%d %d",&m,&n);
    while(n>0)
    {
        int total = n*pow(2,m);
        int total_x = pow(2,m)-1;
        if (total%total_x==0)
            {x = total/total_x;
            break;}
        
        n-=1;
    }
    
    printf("%d\n",n);
    printf("%d",x);
}