#include<bits/stdc++.h>
using namespace std;

int main(){
	long long int t,n,k;
	cin>>t;
	while(t--){
		cin>>n>>k;
		long long int a;
		string s = "";
		for(int i=0;i<n;i++){
			cin>>a;
			if(a%k==0)
				s+="1";
			else
				s+="0";	
		}
		cout<<s<<endl;
		
	}
}
