#include<bits/stdc++.h>
using namespace std;

int main(){
	int t,a,b;
	cin>>t;
	while(t--){
		cin>>a>>b;
		int i=0,l=0,bo=0,j=0;
		string result="";
		while(l<=a && bo<=b){
			if(j%2==0){
				l+=(i+1);
			}
			else{
				bo+=(i+1);
			}
			i++;j++;
		}
		if(l>a){
			result = "Bob";
		}
		else
		result = "Limak";
		cout<<result<<endl;
	}
}
