#include "iostream"
#include "string"
#include "map"
using namespace std;

int main()
{
    map<char, int> m;
    string str, ans;
    int length, i;
    m['B'] = 1, m['F'] = 1,m['P'] = 1,m['V'] = 1,m['C'] = 2,m['G'] = 2,m['J'] = 2,m['K'] = 2,m['Q'] = 2,
    m['S'] = 2, m['X'] = 2,m['Z'] = 2,m['D'] = 3,m['T'] = 3,m['L'] = 4,m['M'] = 5,m['N'] = 5,m['R'] = 6;
    while (cin >> str)
    {
        length = str.size();
        ans = "";
        for (i = 0; i < length; i++)
        {
            if (m[str[i]])
            {
                if (i > 0 && m[str[i]] == m[str[i-1]])//判断是否有相同的soundex
                    continue;
                else
                    ans += m[str[i]] + 48;
            }
        }
        cout << ans << endl;
    }
}