//
// Created by franc on 8/21/2022.
//
#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int a;std::cin>>a;
    int b; std::cin>>b;
    for (int n=a;n<=b;n++){
        if(n<=9){
            std::string numbers[]{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
            std::cout<<numbers[n-1]<<std::endl;
        }
        else std::cout<<((n%2==0)?"even":"odd")<<std::endl;

    }
    return 0;
}
