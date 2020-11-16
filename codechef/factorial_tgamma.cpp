#include<iostream>
#include<math.h>
using namespace std;
int main(){
	int n,res;
	cin>>n;
	res = tgamma(n+1);
	cout<<"Factorial = "<<res;
}
