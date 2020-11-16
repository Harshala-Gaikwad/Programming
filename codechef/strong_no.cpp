#include<iostream>
#include<math.h>
using namespace std;

int factorial(int n){
	int res = tgamma(n+1);
	return res;
}

int main(){
	int n,count=0,a;
	cin>>n;
	int n1;
	n1 = n;
	while(n){
		a = n%10;
		count+=factorial(a);
		n = n/10;
	}
	if(count==n1)
		cout<<"Strong No."<<endl;
	else
	cout<<"Not a Strong No."<<endl;	
	
}
