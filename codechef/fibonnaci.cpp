#include<bits/stdc++.h>
using namespace std;
#define MAX 1000
int fibonnaci(int n){
	int t1 =23,t2=3719,temp;
	for(int i=1;i<=n;i++){
		temp=t1+t2;
		t1=t2;
		t2 = temp;
	}
	cout<<t1;
}
int main(){
	fibonnaci(34);
}
