#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int a[t];
	for(int i=0;i<t;i++)
	{
		int n;
		cin>>n;
		a[i]=n%3;
	}
	for(int i=0;i<t;i++)
	{
		if(a[i]==0)
			cout<<"Anushka";
		else if(a[i]==1)
			cout<<"Bhavana";
		else
			cout<<"Komal";
		cout<<endl;
	}
}
