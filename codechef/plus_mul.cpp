#include<iostream>
using namespace std;
int main(){
	int t,n;
	cin>>t;
	while(t--){
		cin>>n;
		int a[n],count=0;
		for(int i=0;i<n;i++)
			cin>>a[i];
		for(int i=0;i<n;i++){
			for(int j=i+1;j<n;j++){
				if(a[i]+a[j]==a[i]*a[j])
					count++;
			}
		}	
		cout<<count<<endl;
	}
	return 0;
}
