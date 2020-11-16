#include<bits/stdc++.h>
using namespace std;

int main(){
	long int t,a,b,c,x,y;
	cin>>t;
	while(t--){
		long int arr[3];
		for(int i=0;i<3;i++)
			cin>>arr[i];
			cin>>x>>y;
		if(x>y){
			a=y;
			b=x;
		}	
		else{
			a=x;
			b=y;
		}
		sort(arr,arr+3);
        int flag=0;
		if((arr[0]+arr[1]+arr[2])==(x+y)){
			if(a>=arr[0] && b>=arr[1])
				cout<<"YES"<<endl;
			else
				cout<<"No"<<endl;	
		}
		else
			cout<<"NO"<<endl;
	}
}
