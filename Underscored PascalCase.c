#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main()
{
    int n;
    scanf("%d",&n);
    char word[100];
    scanf("%s",word);
    word[0] = toupper(word[0]);
    for(int i =1;i<n;i++)
    {
        strcat(word,"_");
        char word1[100];
        scanf("%s",word1);
        word1[0] = toupper(word1[0]);
        strcat(word,word1);
        
    }
    printf("%s",word);
    return 0;
}