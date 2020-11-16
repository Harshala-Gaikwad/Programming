#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        long long income;
        cin>>income;
        long long tax1=0;
        long long tax2=0;

        if(income<=250000)
            cout<<income<<endl;
            
        else if(income>=250001 && income<=500000)
        {
            income-=250000;
            tax1=(5*income)/100;
            income+=250000;
            cout<<income-tax1<<endl;
        } else if(income>=500001 && income<=750000)
        {
            tax2+=0.05*(250000);
            income-=500000;
            tax1=0.1*(income);
            income+=500000;
            tax2+=tax1;
            cout<<income-tax2<<endl;
        } else if(income>=750001 && income<=1000000)
        {
            tax2+=0.15*(250000);
            income-=750000;
            tax1=0.15*(income);
            income+=750000;
            tax2+=tax1;
            cout<<income-tax2<<endl;
        } else if(income>=1000001 && income<=1250000)
        {
            tax2+=0.3*(250000);
            income-=1000000;
            tax1=0.20*(income);
            income+=1000000;
            tax2+=tax1;
            cout<<income-tax2<<endl;
        } else if(income>=1250001 && income<=1500000)
        {
            tax2+=0.5*(250000);
            income-=1250000;
            tax1=0.25*(income);
            income+=1250000;
            tax2+=tax1;
            cout<<income-tax2<<endl;
        } else if(income>=1500001)
        {
            tax2+=0.75*(250000);
            income-=1500000;
            tax1=0.30*(income);
            income+=1500000;
            tax2+=tax1;
            cout<<income-tax2<<endl;
        }
    }
}
