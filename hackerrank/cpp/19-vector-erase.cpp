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
    int N, x, a, b, tempNum;
    std::vector<int> arr{};
    std::cin>>N;
    for(int i=0;i<N;i++){
        std::cin>>tempNum;
        arr.push_back(tempNum);
    }
    std::cin>>x>>a>>b;
    arr.erase(arr.begin()+x-1);
    arr.erase(arr.begin()+(a-1),arr.begin()+(b-1));
    std::cout<<arr.size()<<std::endl;
    for(int number: arr) std::cout<<number<<" ";
    return 0;
}
