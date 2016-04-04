    #include <stdio.h>  
    #include <stdlib.h>  
    #include <math.h>  
    #include <stack>  
    #include <queue>  
    #include <iostream>  
    #include <string>  

    using namespace std;  
      
      
    int main()  
    {  
        string s;  
        int n, m, i, j, sum;  
        int e[100][100];  
        while(true){  
            cin >> s;  
            if( s == "ENDOFINPUT")            
                break;  
                  
            scanf("%d%d", &m, &n);  
              
            for(i=0; i<m; i++)  
                for(j=0; j<n; j++)  
                    scanf("%1d", &e[i][j]);  
                       
            for(i=0; i<m-1; i++)  
                for(j=0; j<n-1; j++){  
                    sum = e[i][j] + e[i][j+1] + e[i+1][j] + e[i+1][j+1];      
                    e[i][j] = sum / 4;  
                }  
            for(i=0; i<m-1; i++){  
                for(j=0; j<n-1; j++)  
                    printf("%d", e[i][j]);  
                printf("\n");  
            }  
            cin >> s;  
        }  

        return 0;  
    }  