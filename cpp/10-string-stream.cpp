//
// Created by franc on 8/21/2022.
//
#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
    std::stringstream ss(str);
    int number;
    char buffer;
    std::vector<int> numbers;
    while(ss>>number){
        numbers.push_back(number);
        ss>>buffer;
    }
    return numbers;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }

    return 0;
}
