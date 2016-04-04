#!/usr/bin/env python
# -*- coding: utf-8 -*-

#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
int p,s,num;
num=1;
while(scanf("%d%d",&p,&s)!=EOF)
{
   if(p==0&&s==0)
    break;
   printf("Hole #%d\n",num);
   if(s==1)
    printf("Hole-in-one.\n");
   else if(s==p)
    printf("Par.\n");
   else if(p-s==1)
    printf("Birdie.\n");
   else if(p-s==2)
    printf("Eagle.\n");
   else if(p-s==3)
    printf("Double Eagle.\n");
   else if(s-p==1)
    printf("Bogey.\n");
   else if(s-p>=2)
    printf("Double Bogey.\n");
   printf("\n");
   num++;
}
}