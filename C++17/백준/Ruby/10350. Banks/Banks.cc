#include <bits/stdc++.h>
using ll = long long;
using namespace std;
ll s[10010], cnt=0, sum=0, tmp = 0;

int main(){
    ll n;
    scanf("%lld", &n);
    for(int i=0; i<n; i++){
        scanf("%lld", &s[i]);
        sum+=s[i];
    }
    for(int i=0; i<n; i++){
        tmp=0;
        for(int j=i; j<n+i; j++){
            tmp+=s[j%n];
            if(tmp<0){
                cnt+=((-tmp-1)/(sum)+1);
            }
        }
    }
    printf("%lld", cnt);
    return 0;
}