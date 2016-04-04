#include<stdio.h>
#include<stdlib.h> 
int main()
{
  int n,m1,m2,i;
  double a[1005],sum,ave,ave1,ave2,ex1,ex2;
  while(scanf("%d",&n),n){
 sum=0;   ex1=0;   ex2=0;
    for(i=0;i<n;i++){
       scanf("%lf",&a[i]);
       sum+=a[i];
 }
 ave=sum/n;  
 m1=(int)(ave*100);              //注意一定要加括号到ave*100 
    m2=m1;
 ave1=m1*1.0/100.0;              //向下精确到cent 
 if(m2<(ave*100))   m2++;        //向上精确到cent 
    ave2=m2/100.0;   
 for(i=0;i<n;i++){
    if(a[i]<ave)
       ex1+=ave1-a[i];
    else
       ex2+=a[i]-ave2;
 }
 if(ex1>ex2)
      printf("$%.2lf\n",ex1);
 else
   printf("$%.2lf\n",ex2); 
  } 
  system("pause");
  return 0;     
}