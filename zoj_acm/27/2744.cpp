#include "iostream"  
#include "string"  
using namespace std;  
  
string s;  
int len, count;  
void is_palindromes(int i, int j)  
{  
    if (s[i] == s[j])  
    {  
        count++;  
        while (--i >= 0 && ++j < len)  
        {  
            if (s[i] == s[j])  
                count++;  
            else  
                return;  
        }  
    }  
}  
  
int main()  
{  
    int i, j;  
    while (cin >> s)  
    {  
        len = s.length();  
        count = 0;  
        for (i = 1; i <= 2; i++)
            for (j = 0; j < len-i; j++)  
            {  
                is_palindromes(j, j+i);  
            }  
            count += len;
            cout << count << endl;  
            s.clear();  
    }  
}  