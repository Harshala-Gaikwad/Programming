#include<bits/stdc++.h>
using namespace std;
long long int Sum(long long int n,long long int sum){
	sum = (n*(n+1))/2;
	return sum;
}
int main(){
	long long int n,sum=0;
	cin>>n;
	cout<<floor(log10(n)+1)<<endl;
	sum = Sum(n,0);
	cout<<sum;
}
