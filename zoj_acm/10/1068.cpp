#include<stdio.h>  
#include<string.h>  
#include<stdlib.h>  
#include<ctype.h>  
char a[30][6] = {".-","-...","-.-.","-..",".","..-.","--.",  
                 "....","..",".---","-.-",".-..","--","-.",  
                 "---",".--.","--.-",".-.","...","-","..-",  
                 "...-",".--","-..-","-.--","--..",  
                 "..--","---.",".-.-","----"};  
char stoc(char *s)  
{  
    int i;  
    if( strcmp("..--",s)==0 ) return '_';  
    if( strcmp("---.",s)==0 ) return '.';  
    if( strcmp(".-.-",s)==0 ) return ',';  
    if( strcmp("----",s)==0 ) return '?';  
    for( i = 0; i < 26; i++ )  
        if( strcmp(s,a[i]) == 0 ) return 'A'+i;  
}  
int cat( char c,char *s)  
{  
    int m;  
    if( c == '_' ) m = 26;  
    if( c == '.' ) m = 27;  
    if( c == ',' ) m = 28;  
    if( c == '?' ) m = 29;  
    if( isalpha(c) ) m = c-'A';  
    strcat(s,a[m]);  
    return strlen(a[m]);  
}  
int main(void)  
{  
    int i,j,n,cases,fuck,len;  
    int count,t,start,end;  
    char s[110],temp[6];  
    char pro[600];  
    int num[110];  
    while( scanf("%d",&cases) != EOF )  
    for( fuck = 1; fuck <= cases; fuck++)  
    {  
        getchar();  
        scanf("%s",s);pro[0]='/0';  
        len = strlen(s);  
        for( i = 0; i < len; i++ )  
            num[i] = cat(s[i],pro);  
        //puts(pro);  
        for( start=0,end=len-1;start<end;start++,end--)  
           t=num[start],num[start]=num[end],num[end]=t;  
          
        for( i = count = 0; i < len; i++)  
        {  
            for( j= 0; j <num[i];j++)   
                temp[j] = pro[count+j];  
            temp[j] = '/0';  
            pro[i] = stoc(temp);  
            count += strlen(temp);  
        }  
        pro[i] = '/0';  
        printf("%d:",fuck);  
        puts(pro);  
    }  
    return 0;  
}  