#include<bits/stdc++.h>
using namespace std;

int main(){
	long long int n,k;
	cin>>n>>k;
	long long int a[n+1];
	if(n < k) 
		cout << 1;
    else{
        for(int i = 0; i < k; ++i)
			a[i] = 1;
        int sum = k;
        for(int i = k; i < n; ++i){
            a[i] = sum;
            sum = (sum + a[i]) % 1000000007;
            sum = (sum - a[i-k]) % 1000000007;
        }
        cout << a[n-1];
    }
}
