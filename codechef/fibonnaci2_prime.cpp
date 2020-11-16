#include<bits/stdc++.h>
using namespace std;
#define MAX 1000
int fibonnaci(int n){
	int t1 =0,t2=1,temp;
	for(int i=1;i<=n;i++){
		temp=t1+t2;
		t1=t2;
		t2 = temp;
	}
	cout<<t1;
}

int prime(int n){
	int count = 0;
	for(int i=2;i<=MAX;i++){
		int flag =0;
		for(int j=2;j<i;j++){
			if(i%j==0){
				flag = 1;
				break;
			}
		}
		if(flag==0){
			count++;
			if(count==n){
				cout<<i;
				break;
			}
		}
	}
}

int main(){
	int n;
	cin>>n;
	if(n%2 == 1){
		fibonnaci(n/2 + 1);
	}
	else{
		prime(n/2);
	}
	return 0;
}
