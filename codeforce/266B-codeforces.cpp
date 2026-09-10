//  Question  266B

// You are given a queue of n children represented by a string s.
// B = Boy, G = Girl.
// Every second, whenever BG appears, the boy and girl swap positions.
// All swaps for one second happen simultaneously.
// You need to find the queue arrangement after t seconds.
// Constraints: 1 ≤ n, t ≤ 50.

// Problem
// https://codeforces.com/problemset/problem/266/B


// Solution

#include<bits/stdc++.h>
using namespace std;
int main() {
    int n,t;
    cin>>n>>t;
    string student;
    cin>>student;
    for(int i=0;i<t;i++)
    {
        int p=0;
        while(p<n-1)
        {
            if(student[p]=='B' && student[p+1]=='G')
            {
                swap(student[p],student[p+1]);
                p+=2;
            }
            else
            {
                p+=1;
            }
        }
    }
    cout<<student;
    return 0;
}
