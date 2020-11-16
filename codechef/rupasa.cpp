#include<bits/stdc++.h>
using namespace std;

int main(){
	int t,n;
	cin>>t;
	while(t--){
		cin>>n;
		long long int a[n+1];
		cin>>a[0];
		long long int score=0,product=1,sum = a[0];
		for(int i=1;i<=n;i++){
			cin>>a[i];
			score = ((score+sum*a[i])*2)%1000000007;
			sum = (sum+product*a[i])%1000000007;
			product = (product*2)%1000000007;
		}	
		cout<<score<<endl;
	}
}
