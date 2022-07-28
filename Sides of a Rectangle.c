#include <stdio.h>
#include <math.h>
int dist(int x1, int y1, int x2, int y2);
int main()
{
    int x_p1,y_p1,x_p2,y_p2,x_p3,y_p3,x_p4,y_p4;
    scanf("%d %d",&x_p1,&y_p1);
    scanf("%d %d",&x_p2,&y_p2);
    scanf("%d %d",&x_p3,&y_p3);
    scanf("%d %d",&x_p4,&y_p4);
    int flag = 1;
    if (dist(x_p1,y_p1,x_p2,y_p2)==dist(x_p3,y_p3,x_p4,y_p4))
        {
            if (dist(x_p1,y_p1,x_p4,y_p4)==dist(x_p2,y_p2,x_p3,y_p3))
            {
                if (dist(x_p4,y_p4,x_p2,y_p2)==dist(x_p1,y_p1,x_p3,y_p3))
                {
                    flag = 0;
                    printf("Yes");
                }
            }
        }
    if (flag==1)
        printf("No");
    return 0;
}
int dist(int x1,int y1,int x2,int y2)
    {
        int d = pow((pow((x2-x1),2)+pow((y2-y1),2)),0.5);
        return d;
    }