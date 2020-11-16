#include<iostream>
using namespace std;
int main(){
	int t,n,k,v;
	cin>>t;
	while(t--){
		cin>>n>>k>>v;
		int a[n],sum;
		for(int i=0;i<n;i++)
			cin>>a[i];
		sum = n+k;
		sum = sum*v;
		int count =0;
		for(int i=0;i<n;i++)
			count = count+a[i];
		int result = sum-count,x;
		if(result>0){
			x = result%k;
			if(x==0)
				cout<<result/k<<endl;
			else
				cout<<-1<<endl;	
		}		
		else
			cout<<-1<<endl;
		
	}
	
}
