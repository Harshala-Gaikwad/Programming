#include<bits/stdc++.h>
using namespace std;

int main(){
	int t,n;
	cin>>t;
	while(t--){
		cin>>n;
		int a[n],c,flag=0;
		double total=0,total2 = 0,avg2,avg;
		for(int i=0;i<n;i++){
			cin>>a[i];
			total += a[i];
		}
		avg = total/n;
		for(int i=0;i<n;i++){
			total2 = total-a[i];		
			avg2 = total2/(n-1);
			if(avg == avg2){
				//cout<<a[i]<<endl;
				flag =1;
				c = i+1;
				break;
			}
		}
		if(flag==1)
		cout<<c<<endl;
		else
		cout<<"Impossible"<<endl;
	}
}
