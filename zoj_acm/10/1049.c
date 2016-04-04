#include <stdio.h>
#include <math.h> 
#define  PI   3.1415926

int main()
{
	int n,i=0,j=1;
	float fx,fy;
	scanf("%d",&n);
	while(j<=n)
	{
		scanf("%f%f",&fx,&fy);
		for(i=0;;i++)
		{
			if(i*100/PI<pow(fx,2)+pow(fy,2)&&(i+1)*100/PI>=pow(fx,2)+pow(fy,2))
			{
				printf("Property %d: This property will begin eroding in year %d.\n",j,i+1);
				break;

			}

		}
		j++;

	}
	printf("END OF OUTPUT.\n");

	return 0;
}