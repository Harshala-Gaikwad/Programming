#include<bits/stdc++.h>
using namespace std;

int main(){
	int t,C,D,L;
	cin>>t;
	while(t--){
		cin>>C>>D>>L;
    	int r1=(C+D)*4,r2;
	    if(C>(2*D))
        {
            r2=(D+(C-(2*D)))*4;
        }
        else{
            r2=D*4;
        }
	    if(L<=r1&&L>=r2&&L%4==0)
	    cout<<"yes"<<endl;
	    else 
		cout<<"no"<<endl;
	}
}
