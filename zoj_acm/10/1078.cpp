#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;
int main()
{
	int n;
	int i,j;
	while(scanf("%d",&n)&&n)
	{
		int flag=0;//sign of palindrom
		char c[30];//number stored in bit
		int base[17]={0};//scale of panlindrom
		for(i=2;i<=16;i++)//2~16 scale
		{
			int m=n;
			int len=0;
			while(m)
			{
				c[len++]=m%i;
				m=m/i;
			}
			//estimate whether it is palindrom
			flag=1;
			for(j=0;j<len/2&&flag;j++)
				if(c[j]!=c[len-j-1]) flag=0;//it is not palindrom
			if(flag) base[i]=1;
		}
		flag=1;
		for(i=2;i<=16;i++)
			if(base[i]==1) flag=0;//there exist a palindrom
		//there is no palindrom
		if(flag) printf("Number %d is not a palindrom\n",n);
		else
		{//at least 1 palindrom
			printf("Number %d is palindrom in basis",n);
			for(i=2;i<=16;i++)
				if(base[i]==1) printf(" %d",i);
			puts("");
		}
	}
	return 0;
}
