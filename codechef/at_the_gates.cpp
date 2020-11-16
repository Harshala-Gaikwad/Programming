#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--)
	{
	    int n,k,count=0;
	    cin>>n>>k;
	    char a[n];
	    for(int i=0;i<n;i++)
	        cin>>a[i];
	    while(k)
	    {	if(a[n-1]=='H')
	        {
	            for(int i=0;i<n-1;i++)
        	    {
        	        if(a[i]=='H')
        	        {
        	            a[i]='T';
        	        }
        	        else
        	        {
        	             a[i]='H';
        	        }
        	    }
	        }
	        k--;
	        n--;
	    }
	    for(int i=0;i<n;i++)
	    {
	        if(a[i]=='H')
               count++;
	    }
	    cout<<count<<endl;
	    
	}
	return 0;
}

