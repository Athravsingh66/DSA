// Question

// Given a year y between 1000 and 9000, find the smallest year greater than y whose all four digits are different.

// The answer must be strictly greater than y.
// No digit can appear more than once in the year.
// Print that minimum valid year.
// An answer is guaranteed to exist.

// Problem
// https://codeforces.com/problemset/problem/271/A


// Solution

#include<bits/stdc++.h>
using namespace std;
int main() {
    int year;
    cin>>year;
    while (true)
    {
        year++;
        string s=to_string(year);
        set<char>digit(s.begin(),s.end());
        if (digit.size()==s.size())
        {
            cout<<year;
            break;
        }
    }
    return 0;
} 

    