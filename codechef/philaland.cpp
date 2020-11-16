#include<bits/stdc++.h>
using namespace std;

int main(){
	long int t,n;
	cin>>t;
	while(t--){
		cin>>n;
		int i=0;
		while(n>=1){
			n=floor(n/2);
			i++;
		}
		cout<<i<<endl;
	}
}
