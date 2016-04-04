#!/usr/bin/env python
# -*- coding: utf-8 -*-

#include<stdio.h>
#include<string.h>

#include<stdio.h>
#include<string.h>

int main(void)
{
int ncases,m;
while(scanf("%d",&ncases) != EOF)
{
while(ncases--)
{
scanf("%d",&m);
if( m==1 ) printf("7\n");
if( m==2 ) printf("27\n");
if( m>2 && m<=10 ) printf("70\n");
if( m==11 ) printf("270\n");
if( m>=12 && m<100 ) printf("700\n");
}
}
return 0;
}