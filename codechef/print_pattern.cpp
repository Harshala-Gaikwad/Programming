#include<bits/stdc++.h>
using namespace std;

int main(){
	 int t,n;
	cin>>t;
	while(t--){
		cin>>n;
		int a[n][n],f=1;
		for(int i=0;i<(2*n);i++){
			for(int j=0;j<n;j++){
				int temp = i-j;
				if(0<=temp && temp<n){
					a[j][temp]=f;
					f++;
				}
			}
		}
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				cout<<a[i][j]<<" ";
			}
			cout<<endl;
		}
	}
}
