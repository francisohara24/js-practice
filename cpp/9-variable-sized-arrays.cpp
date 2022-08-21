//
// Created by franc on 8/21/2022.
//
#include <vector>
#include <iostream>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n,q,k,i,j;
    std::vector<std::vector<int>> arr{};
    std::cin>>n>>q;
    for(int i=0;i<n;i++){
        std::vector<int> tempArr{};
        std::cin>>k;
        int tempNum;
        for(int j=0;j<k;j++){
            std::cin>>tempNum;
            tempArr.push_back(tempNum);
        }
        arr.push_back(tempArr);
    }
    for(int k=0;k<q;k++){
        std::cin>>i>>j;
        std::cout<<arr[i][j]<<std::endl;
    }
    return 0;
}
