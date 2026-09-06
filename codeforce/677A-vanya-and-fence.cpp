// Question

// Given n people's heights and a fence height h, calculate the minimum
// road width needed. Height <= h requires width 1, otherwise width 2.

// Problem
// https://codeforces.com/problemset/problem/677/A

// Solution

#include<bits/stdc++.h>
using namespace std;
int main() {
    int count=0,i,n,h;
    cin>>n>>h;
    for(i=0;i<n;i++)
    {
        int a;
        cin>>a;
        if(a>h)
        {
            count+=2;
        }
        else
        {
            count+=1;
        }
    }
    cout<<count;
    return 0;
}


