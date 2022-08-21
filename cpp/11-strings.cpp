//
// Created by franc on 8/21/2022.
//
#include <iostream>
#include <string>


int main() {
    std::string a;
    std::string b;
    std::cin>>a>>b;
    std::cout<<a.size()<<" "<<b.size()<<std::endl;
    std::cout<<a+b<<std::endl;
    std::cout<<b[0]+a.substr(1)<<" "<<a[0]+b.substr(1);


    return 0;
}
