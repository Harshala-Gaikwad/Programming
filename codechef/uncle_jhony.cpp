#include<bits/stdc++.h>
using namespace std;
int main(){
	int t,n,k;
	cin>>t;
	while(t--){
		cin>>n;
		int a[n];
		for(int i=0;i<n;i++)
			cin>>a[i];
		cin>>k;
		int max = a[k-1],pos=0;
		sort(a,a+n);
		for(int i=0;i<n;i++){
			if(a[i]==max)
			pos = i;
		}
		cout<<pos+1<<endl;
	}
}
