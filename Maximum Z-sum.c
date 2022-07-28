#include <stdio.h>
int main()
{
    int r,c;
    scanf("%d %d",&r,&c);
    int matrix[r][c];
    for(int i=0;i<r;i++)
        {
            for(int j =0;j<c;j++)
                scanf("%d",&matrix[i][j]);
        }

    int max_z_sum = 0;
    int count =0;
    int ele[r][2];
    for(int i=0;i<r-1;i++)
        {
            for(int j =0;j<c-1;j++)
            {
                int z_sum=matrix[i][j]+matrix[i][j+1]+matrix[i+1][j]+matrix[i+1][j+1];
        
                if (z_sum>max_z_sum)
                    {
                        count =0;
                        max_z_sum = z_sum;
                        ele[0][0]= i+1;
                        ele[0][1]=j+1;
                        
                    }
                else if (z_sum==max_z_sum)
                    {
                        count++;
                        ele[count][0]= i+1;
                        ele[count][1]= j+1;
                    }
            }
        }
        

    printf("%d\n",max_z_sum);
    for (int q =0;q<r;q++)
    {
       int i = ele[q][0];
        int j = ele[q][1];
       if (i<r && i>0 && j<c &&j>0)
            {
                i--;
                j--;
                printf("%d\t%d\n",i+1,j+1);
                printf("%d\t%d\t%d\t%d\n",matrix[i][j],matrix[i][j+1],matrix[i+1][j],matrix[i+1][j+1]);
            }
    }
    
    return 0;
}