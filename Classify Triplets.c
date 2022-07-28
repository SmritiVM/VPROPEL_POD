#include <stdio.h>
char* pythagorean(int a,int b,int c)
    {int diff = c*c-(a*a+b*b); 
    if (diff==0)
        return "Exactly Pythagorean";
    else if (diff==1|diff==-1)
        return "Very Close to Pythagorean";
    else if (diff==2|diff==-2)
        return "Close to Pythagorean";
    else
        return "False";}

int main()        
{
    int l,u;
    scanf("%d %d",&l,&u);
    for(int i =l;i<u+1;i++)
    {for (int j=i;j<u+1;j++)
        {for (int k=j;k<u+1;k++)
            {if (pythagorean(i,j,k)!="False")
                printf("%d %d %d %s\n",i,j,k,pythagorean(i,j,k));}}}
    return 0;}