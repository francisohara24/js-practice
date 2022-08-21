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
    int N;std::cin>>N;
    int arr[N];
    for(int i=0;i<N;i++) std::cin>>arr[i];
    for(int i=0;i<N;i++) std::cout<<arr[N-i-1]<<" ";
    return 0;
}
