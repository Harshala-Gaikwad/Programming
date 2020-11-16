#include
void main()
{
int n; // for number of lines of nxn matrix
int result;
int maze[20][20]; // max 20×20 matrix
int i,j;

printf(“\nEnter n value: “);
scanf(“%d”,&n);
printf(“Enter %d x %d values for matrix starting with 1\n”,n,n);
for(i=1;i<=n;i++)
for(j=1;j<=n;j++)
scanf("%d",&maze[i][j]);

result = 1;
i=1;j=1;
while(i<=n && j<=n)
{
if(i == n) {
while(j<n) {
if(maze[i][j+1] < result) {
j++;
}
else {
result = maze[i][j++];
j++;
}
}
i=n+1;
j=n+1;
}

else if(j == n) {
while(i<n) {
if(maze[i+1][j] < result) {
i++;
}
else {
result = maze[i+1][j];
i++;
}
}
i=n+1;
j=n+1;
}

else {
if(maze[i][j+1] < maze[i+1][j]) {
if(maze[i][j+1] < result) {
j++;
}
else {
result = maze[i][j+1];
j++;
}
}
else {
if(maze[i+1][j] < result) {
i++;
}
else {
result = maze[i+1][j];
i++;
}
}
}
}
printf("\nResult weight is: %d",result);
