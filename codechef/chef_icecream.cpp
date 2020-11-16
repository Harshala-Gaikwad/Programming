#include<bits/stdc++.h>
using namespace std;

int main(){
	int t,n;
	cin>>t;
	while(t--){
		cin>>n;
		int a[n],x=0,flag=1,y=0,z=0;
		for(int i=0;i<n;i++){
			cin>>a[i];
		}
		for(int j=0;j<n;j++)
        {
            if(a[j]==5)
            x++;
            
            else if(a[j]==10)
            {
                if(x<1)
                { flag=0;
                  break;
				}
                x--;
                y++; 
            }
            
            else if(a[j]==15)
            {
                if(y>=1)
                {
                    y--;
                    
                }
                
                else if(x>=2)
                {
                    x=x-2;
                }
                
                else
                {
                    flag=0;
                    break;
                }                
            }
        }
        if(flag==1)
        cout<<"YES\n";
        else
        cout<<"NO\n" ;
    }
}
