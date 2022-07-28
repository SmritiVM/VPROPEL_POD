#include <stdio.h>
#include <string.h>

int main()
{
    
    int n;
    scanf("%d",&n);
    char rocks[100]="";
    for(int i =0;i<n;i++)
        {char mineral[100];
        scanf("%s",mineral);
        strcat(rocks,mineral);}
        
    int freq[256] = {0};
    char result;
    int len = strlen(rocks);
    int max=-1;
    int i;
    for(i = 0; i < len; i++)
  	{
  		freq[rocks[i]]++;
	}
  		
  	for(i = 0; i < len; i++)
  	{
		if(max < freq[rocks[i]])
		{
			max = freq[rocks[i]];
			result = rocks[i];
		}
	}
    printf("%c",result);
    return 0;
}