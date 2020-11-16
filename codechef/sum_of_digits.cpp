#include<iostream>
using namespace std;
int main(){
	int n;
	cin>>n;
	int sum=0,a;
	while(n){
		a = n%10;
		sum +=a;
		n = n/10;
	}
	cout<<sum;
}
