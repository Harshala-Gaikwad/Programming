#include<bits/stdc++.h>
using namespace std;

int main(){
	int T,N,U,D;
	cin>>T;
	while(T--){
		cin>>N>>U>>D;
		int H[N];
		for(int i=0;i<N;i++)
			cin>>H[i];
		int flag =0,count =0;
		for(int i=1;i<N;i++){
			if(H[i]>H[i-1]){
				if(H[i]-H[i-1]<=U)
					count =i;
				else break;	
			}
			else{
				if(H[i-1]-H[i]<=D)
					count =i;
				else if(flag==0){
					count =i;
					flag=1;
				}
				else break;	
			}
		}cout<<count+1<<endl;	
			
	}
}


/*
bool used=false;
		int ret=0;
		for (int i=1; i<N; i++) {
			if(H[i]>H[i-1]) {
				if(H[i]-H[i-1]<=U) ret=i;
				else break;
			} else {
				if(H[i-1]-H[i]<=D) ret=i;
				else if(!used) ret=i, used=true;
				else break;
			}
		}
		cout<<ret+1<<"\n"; */
