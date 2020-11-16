#include <iostream>
using namespace std;
int sum_of_natural_numbers(int n)
{
int sum = 0;
sum = (n*(n+1))/2;
return sum;
}
int main()
{
int n;

cin >> n;

cout <<sum_of_natural_numbers(n);
cout << endl;
return 0;
}


