//
// Created by franc on 8/21/2022.
//
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int N; std::cin>>N;
    std::vector<int> arr;
    int tempNum;
    for(int i=0;i<N;i++) {
        std::cin>>tempNum;
        arr.push_back(tempNum);
    }
    std::sort(arr.begin(), arr.end());
    for(int number: arr) std::cout<<number<<" ";
    return 0;
}
