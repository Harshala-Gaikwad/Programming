#include <iostream>
#include <algorithm>

// Naive method to find a pair in an array with given sum
void findPair(int arr[], int n, int sum)
{
	// consider each element except last element
	std::sort(arr,arr+n);
	int low = 0;
	int high = n-1;
	while(low<high){
		if((arr[low]+arr[high])==sum){
			printf("Pair found at index %d and %d",low,high);
			return;
		}
		(arr[low]+arr[high]<sum)?low++:high--;
	}
	printf("Pair not found");
}

int main()
{
	int arr[] = { 8, 7, 2, 5, 3, 1 };
	int sum = 10;

	int n = sizeof(arr)/sizeof(arr[0]);

	findPair(arr, n, sum);

	return 0;
}
