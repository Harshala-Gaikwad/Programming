#include<bits/stdc++.h>
using namespace std;

int main(){
	int t,n,income;
	cin>>t;
	while(t--){
		cin>>n;
		if(n<=250000)
			income = n;
		else if(n>250000 && n<=500000)
			income = n-(n*0.05);
		else if(n>500000 && n<=750000)
			income = n-(n*0.1);
		else if(n>750000 && n<=1000000)
			income = n-(n*0.15);
		else if(n>1000000 && n<=1250000)
			income = n-(n*0.2);
		else if(n>1250000 && n<=1500000)
			income = n-(n*0.25);
		else 
			income = n-(n*0.3);					
	    cout<<income<<endl;				
	}

}
