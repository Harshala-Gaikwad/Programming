#include<iostream>
using namespace std;
class area(){
	int r,A;
	int Area();
};

int area::Area(){
	A = 3.14*r*r;
	return A;
}

int main(){
	area b1;
	b1.r = 2;
	a = b1.Area();
	cout<<"Area="<<a;
	return 0;
}
