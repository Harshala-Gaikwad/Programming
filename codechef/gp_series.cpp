#include<iostream>
using namespace std;

int main(){
	int n,s1,s2;
	cout<<"Enter the number of terms : ";
	cin>>n;
	cout<<"Enter the common ratio for G.P - 1 : ";
	cin>>s1;
	cout<<"Enter the common ratio for G.P - 2 : ";
	cin>>s2;
	cout<<"The series is:\n";
	int a=1,b=1;
	if(n%2==0){
		for(int i=0;i<n/2;i++){
			cout<<a<<" ";
			a = a*s1;
			cout<<b<<" ";
			b = b*s2;
		}
	}
	else{
		for(int i=0;i<n/2;i++){
			cout<<a<<" ";
			a = a*s1;
			cout<<b<<" ";
			b = b*s2;
		}cout<<a;
	}
}
