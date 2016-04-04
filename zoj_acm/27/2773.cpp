#!/usr/bin/env python
# -*- coding: utf-8 -*-

#include <iostream>  
using namespace std;  
  
int main()  
{  
    int n;   
    cin>>n;  
    int i = 0;  
    while(n--)  
    {  
        int num;  
        cin>>num;  
        i++;  
        long  r = 0; //在这里使用int/long/long long 都可以通过  
        for(int k = 1; k <= num; k++)  
        {  
            r += (k*(k+1)*(k+2)/2);  
        }  
        cout<<i<<" "<<num<<" "<<r<<endl;  
    }  
    return 0;  
}  