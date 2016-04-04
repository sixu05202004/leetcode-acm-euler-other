#include <iostream>  
#include <cstdio>  
#include <cmath>  
using namespace std;  
  
int main()  
{  
    int cookie, temp;  
    bool first = true;  
    while(scanf("%d", &cookie) != EOF){  
        if(cookie == 5280){  
            scanf("%d", &temp);  
            break;  
        }  
        if(!first){  
            printf("\n");  
        }  
        if(first){  
            first = false;  
        }  
        int location = 0;  
        while(location != cookie){  
            scanf("%d", &temp);  
            printf("Moving from %d to %d: ", location, temp);  
            if(temp == cookie){  
                printf("found it!\n");  
                break;  
            }  
            if(fabs(fabs(temp-cookie)-fabs(location-cookie)) < 1e-3){  
                printf("same.\n");  
            }  
            else{  
                if(fabs(temp-cookie) < fabs(location-cookie)){  
                    printf("warmer.\n");  
                }  
                if(fabs(temp-cookie) > fabs(location-cookie)){  
                    printf("colder.\n");  
                }  
            }  
            location = temp;  
        }  
    }  
    return 0;  
}  