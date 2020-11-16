#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin >> t;
	int n,a,b,c,d,p,q,y;
	int A[301];
    A[0] = 0;
    int t1=0, t2=0;

	while(t--){
        cin >> n >> a >> b >> c >> d >> p >> q >> y;
	    for(int j=1; j<(n+1); j++){
	        cin >> A[j];
	    }
	     t1 = abs(A[b] - A[a])*p;
	     t2 = abs(A[c] - A[a])*p;
	    if(t2 > y){
	        cout << t1 << endl;
	    }
	    else{
	        t2 = y + abs(A[d] - A[c])*q;
	        t2 += abs(A[b] - A[d])*p;
	        if(t1 < t2){
	            cout << t1 << endl;
	        }
	        else{
	            cout << t2 << endl;
	        }
	    }


	}

	return 0;
}

