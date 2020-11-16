#include<bits/stdc++.h>
using namespace std;

int main(){
	int T,a,b,c,d;
	cin>>T;
	while(T--){
		cin>>a>>b>>c>>d;
		if(c==d){
			if(a==b)
				cout<<"YES"<<endl;
			else
				cout<<"NO"<<endl;	
		}
		else{
			if(b<a)
				swap(a,b);
			if(d<c)
				swap(c,d);
			if((b-a)%(c-d)==0){
				cout<<"YES"<<endl;
			}		
			else{
				cout<<"NO"<<endl;
			}
		}
	}
}
