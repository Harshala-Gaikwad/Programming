#include<iostream>
using namespace std;
int main(){
	int n;
	cin>>n;
	int sum=0,a,rev;
	while(n){
		a = n%10;
		rev = (rev*10)+a;
		n = n/10;
	}
	cout<<rev;
}
