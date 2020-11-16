#include<bits/stdc++.h>
using namespace std;

int main(){
	int t,n;
	cin>>t;
	while(t--){
		int x=0,y=0;
		cin>>n;
		string s;
		cin>>s;
		if (s[0]=='L')
			x-=1;
		else if (s[0]=='R')
			x+=1;
		else if (s[0]=='U')
			y+=1;
		else if (s[0]=='D')
			y-=1;
		for(int i=1;i<n;i++){
			if(s[i-1]=='L'|| s[i-1]=='R'){
				if(s[i]=='U')
					y+=1;
				if(s[i]=='D')
					y-=1;	
			}
			else if(s[i-1]=='U'|| s[i-1]=='D'){
				if(s[i]=='L')
					x-=1;
				if(s[i]=='R')
					x+=1;	
			}
		}			
		cout<<x<<" "<<y<<endl;	
	}
}
