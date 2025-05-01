#include<stdio.h>
int main(){
	int n,a,b,d=1e9;
	scanf("%d",&n);
	while(n--){
		scanf("%d %d",&a,&b);
		if(a<=b&&b<d) d=b;
	}
	printf("%d",(d==1e9)?-1:d);
}