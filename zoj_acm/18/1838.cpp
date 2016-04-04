#include <iostream>  
#include <cstdio>  
#include <string>  
#include <string.h>  
#include <map>  
using namespace std;  
string s[110];  
string model="the quick brown fox jumps over the lazy dog";  
map <char,char>mp;  
  
bool ok( int k )  
{  
    int i;  
    map <char,char>temp;  
    for( i=0;i<s[k].size();i++ )  
    {  
        if( s[k][i]==' ' )  
        {  
            if( model[i]!=' ' ) return false;  
            else continue;  
        }  
        if( temp.find( s[k][i] )!=temp.end() )  
        {  
            if( temp[ s[k][i] ]!=model[i] )  
                return false;  
        }  
        else temp[ s[k][i] ]=model[i];  
    }  
    return true;  
}  
  
bool solve( int m,int n )  
{  
    int i,j;  
    for( i=0;i<m;i++ )  
        if( s[i].size()==n && ok(i) )  
        {  
            for( j=0;j<n;j++ )  
                mp[ s[i][j] ]=model[j];  
            return true;  
        }  
    return false;  
}  
  
int main()  
{  
    int i,j,m,n,T=1;  
    n=model.size();  
    while( getline( cin,s[0] ) )  
    {  
        if( s[0]=="" )  break;  
        i=1;  
        while( getline( cin,s[i] ) && s[i]!="" )  
            i++;  
        m=i;  
        if( T!=1 )  cout<<endl;  
        if( solve( m,n ) )  
        {  
            for( i=0;i<m;i++ )  
            {  
                for( j=0;j<s[i].size();j++ )  
                {  
                    if( s[i][j]==' ' )   continue;  
                    s[i][j]=mp[ s[i][j] ];  
                }  
                cout<<s[i]<<endl;  
            }  
        }  
        else cout<<"No solution.\n";  
        mp.clear();  
        T++;  
    }  
    return 0;  
} 