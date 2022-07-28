#include <stdio.h>
#include <string.h>
#include <math.h>
int bin_conv(int m,char n[25]);
int beep(int m, char n[25]);

int main()
{
    char n[25];
    scanf("%s",n);
    int m = strlen(n);
    int beep_count = 0;
    for(int i=0;i<m-1;i++)
    {
        if (beep(m,n)==1)
            beep_count++;
        char temp[m];
        temp[0]=n[m-1];
        for(int j=1;j<m;j++)
            temp[j]=n[j-1];
        strcpy(n,temp);
    }
    printf("%d\n",beep_count);
    return 0;
    
}

int bin_conv(int m, char n[25])
{
    int multiplier = 0;
    int dec_num = 0;
    for(int i=m-1;i>=0;i--)
        {
            int x = (int)n[i]-48;
            dec_num+=pow(2,multiplier)*x;
            multiplier+=1;
        }
    return dec_num;
}

int beep(int m,char n[25])
{
    int dec_num = bin_conv(m,n);
    if (dec_num%2==0)
       return 1;
    else
        return 0;
}