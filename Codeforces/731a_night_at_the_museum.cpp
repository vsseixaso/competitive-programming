#include<bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define PI acos(-1.0)
#define INF 0x3f3f3f3f
typedef long long LL;
typedef unsigned long long ULL;

int ans;
char s[200];

int main()
{
    scanf("%s",s);
    int len=strlen(s);
    int t='a';
    ans=0;
    for(int i=0;i<len;i++){
        ans+=min((t-s[i]+26)%26,(s[i]-t+26)%26);
        t=s[i];
    }
    printf("%d\n",ans);
    return 0;
}