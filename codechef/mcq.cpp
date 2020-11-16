#include<bits/stdc++.h>
using namespace std;

int main(){
	int t,n;
	cin>>t;
	while(t--){
		cin>>n;
		string s1,s2;
		cin>>s1;
		cin>>s2;
		int a[n], count=0;
		for(int i=0;i<n;i++)
			a[i]=i;
		for(int i=0;i<n;i++){
			if(a[i]!=-1){
				if(s1[i]==s2[i])
					count++;
			
			if(s1[i]!=s2[i] && s2[i]!='N')
				a[i+1]=-1;
		}
		}
		cout<<count<<endl;		
	}
}
