#include<bits/stdc++.h>
using namespace std;

int main(){
	int t,n;
	cin>>t;
	while(t--){
		cin>>n;
		string s1,s2;
		int c1=0,c2=0,c3=0,c4=0;
		cin>>s1>>s2;
		for(int i=0;i<n;i++){
			if(s1[i]=='0')
				c1++;
			else
				c2++;	
		}
		for(int i=0;i<n;i++){
			if(s2[i]=='0')
				c3++;
			else
				c4++;	
		}
		if((c1==c3)&&(c2==c4))
			cout<<"YES"<<endl;
		else
			cout<<"NO"<<endl;	
	}
}
