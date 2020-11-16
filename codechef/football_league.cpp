#include<bits/stdc++.h>
using namespace std;

struct Teams{
	string Name;
	int match_played,gf,ga,gd,points,rank;
};

bool cmp(Teams x,Teams y){
	return x.points>y.points;
}

int main(){
	int n,m,S1,S2;
	string temp,T1,T2;
	cin>>n;
	Teams a[n];
	for(int i=0;i<n;i++){
		a[i].match_played=0;a[i].gf=0;a[i].ga=0;a[i].points=0;
	}
	for(int i=0;i<n;i++){
		cin>>a[i].Name;
	}
	cin>>m;
	for(int i=0;i<m;i++){
		cin>>T1>>T2>>S1>>S2;
		for(int j=0;j<n;j++){
			temp = a[j].Name;
			if(temp == T1){
				a[j].gf += S1;
				a[j].ga += S2;
				a[j].match_played+= 1;
				if(S1>S2)
					a[j].points += 2;
				else if(S1==S2)
					a[j].points += 1;	
			}
			if(a[j].Name==T2){
				a[j].gf += S2;
				a[j].ga += S1;
				a[j].match_played += 1;
				if(S1<S2)
					a[j].points += 2;
				else if(S1==S2)
					a[j].points += 1;	
			}
		}
	}
	for(int i=0;i<n;i++){
		if(a[i].match_played>2){
			cout<<"Invalid input"<<endl;
			return 0;
		}
	}
	for(int i=0;i<n;i++){
		a[i].gd = a[i].gf-a[i].ga;
	}
	sort(a,a+n,cmp);
	for(int i=0;i<n;i++){
		cout<<a[i].Name<<" "<<a[i].match_played<<" "<<a[i].gf<<" "<<a[i].ga<<" "<<a[i].gd<<" "<<a[i].points<<endl;
	}
}
