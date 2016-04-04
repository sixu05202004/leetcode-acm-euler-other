#include<stdio.h>  
int main(){  
    char w[7][10]={"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday" ,"Saturday"};  
    int m[2][13]={0,31,28,31,30,31,30,31,31,30,31,30,31,  
                  0,31,29,31,30,31,30,31,31,30,31,30,31};  
    int yd[2]={365,366};  
    long day;  
    int year,month,week;  
    int i,j,flag;  
    while(scanf("%ld",&day)&&-1!=day){  
        week=(day+6)%7;//得到星期几   
        year=2000;  
        flag=(0==year%4&&year%100!=0)||0==year%400;//flag=1为闰年   
        ++day;//题目说经过多少天，所以在这里先加1   
        for(;day>yd[flag];){//得到年份、剩余天数   
            day-=yd[flag];   
            year++;  
            flag=(0==year%4&&year%100!=0)||0==year%400;  
        }  
        for(month=1;day>m[flag][month];++month){//得到月份和对应天数   
            day-=m[flag][month];  
        }  
        printf("%d-%02d-%02d %s\n",year,month,day,w[week]);//%02d很方便:如果整数不够2列就补上0          
    }  
}