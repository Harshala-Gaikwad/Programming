#include<bits/stdc++.h>
using namespace std;

int main(){
	int T,N;
	cin>>T;
	while(T--){
		cin>>N;
		int S[N],i;
		for(i=0;i<N;i++)
			cin>>S[i];
		S[0]=abs(S[1]-S[0])-1;	
		for(i=1;i<N-1;i++){
			S[0]+=abs(S[i+1]-S[i])-1;
		}	
		cout<<S[0]<<endl;
	}
}
