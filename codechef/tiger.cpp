#include<bits/stdc++.h>
using namespace std;

int main(){
	int t,f,d,a,v;
	cin>>t;
	while(t--){
		cin>>f>>d>>a>>v;
		int t1,t2;
		t1 = sqrt((2*(f+d))/a);
		t2 = f/v;
		if(t1<=t2)
		cout<<"Tiger"<<endl;
		else
		cout<<"Bolt"<<endl;
	}
}
