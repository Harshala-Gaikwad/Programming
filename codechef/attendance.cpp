#include<bits/stdc++.h>
using namespace std;

int main(){
	int t,n;
	cin>>t;
	while(t--){
		cin>>n;
		int a[n];
		string s1[n],s2[n];
		for(int i=0;i<n;i++){
			a[i]=0;
			cin>>s1[i]>>s2[i];
		}
		for(int i=0;i<n;i++){
			for(int j=i+1;j<n;j++){
				if(s1[i]==s1[j]){
					a[i]++;
					a[j]++;
				}
			}
		}
		for(int i=0;i<n;i++){
			if(a[i]>0)
			cout<<s1[i]<<" "<<s2[i]<<endl;
			else
			cout<<s1[i]<<endl;			
		}
	}
}
