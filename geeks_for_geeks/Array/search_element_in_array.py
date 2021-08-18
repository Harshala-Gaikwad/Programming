#User function Template for python3

#Complete the below function
def search(arr, N, X):
    #Your code here
    for i in range(N):
        if arr[i]==X:
            return i
    return -1 
