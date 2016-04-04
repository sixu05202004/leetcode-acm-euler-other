#include <stdio.h>
#include <string.h>
char f[10000];
int main(void)
{
    int k, m, cou_ch, ok, c, r, count;
    int i, j;
   
    while (scanf("%d", &k) != EOF && k)
    {
        scanf("%d", &m);
        memset(f, 0, sizeof(f));
        ok = 1;
       
        for (i = 0; i < k; i++)
        {
            scanf("%d", &cou_ch);
            f[cou_ch] = 1;
        }
       
       
        for (i = 0; i < m; i++)
        {
            count = 0;
            scanf("%d %d", &c, &r);
           
            for (j = 0; j < c; j++)
            {
                scanf("%d", &cou_ch);
                if (f[cou_ch]) count++;
            }
            if (count < r) ok = 0;
        }
       
        if (ok) printf("yes\n");
        else printf("no\n");
    }
    return 0;
}