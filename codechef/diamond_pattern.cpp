#include<iostream>
using namespace std;

int main(){
	int n=15,x=1,j=1;
	for(int i=1;x<=n;){
		if(!(j<=i)){
			cout<<endl;
			j=1;
			i++;
		}
		else{
			cout<<"*";
			x++;j++;
		}
	}
}
