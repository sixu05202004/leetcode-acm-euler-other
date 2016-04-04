#include <iostream>
using namespace std;
int main()
{
	int n,a,b,x,y;
	cin>>n;
	while(cin>>a>>b)
	{
		x=(a+b)/2;
		y=(a-b)/2;
		if(x>=0&&y>=0&&(a+b)%2==0)
			cout<<x<<' '<<y<<endl;
		else
			cout<<"impossible"<<endl;
	}
	return 0;
}