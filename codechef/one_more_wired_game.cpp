#include<iostream>
using namespace std;

int main(){
	int t,n,m;
	cin>>t;
	while(t--){
		cin>>n>>m;
		cout<<n*(m-1)+m*(n-1)<<endl;
	}
}
