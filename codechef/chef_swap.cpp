#include<bits/stdc++.h>
using namespace std;

int main(){
	long long int t,n,i,j;
	cin>>t;
	while(t--){
		cin>>n;
		long long int a[n],b[n];
		for(i=0;i<n;i++)
			cin>>a[i];
		for(i=0;i<n;i++)
			cin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		if(a==b){
			cout<<"yes"<<endl;
		}
		else
			cout<<"no"<<endl;
		for(i=0;i<n;i++)
			cout<<a[i]<<" ";
			cout<<"\n";
		for(i=0;i<n;i++)
			cout<<b[i]<<" ";		
	}
}
