#include<bits/stdc++.h>
using namespace  std;

int main(){
	int t,n,k;
	cin>>t;
	while(t--){
		cin>>n>>k;
		int d = n/k;
		if(d%k==0){
			cout<<"NO"<<endl;
		}
		else
		cout<<"YES"<<endl;
	}
}
