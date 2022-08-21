//
// Created by franc on 8/21/2022.
//
#include <iostream>

class Student{
public:
    int scores[5];
    void input(){
        for(int i=0;i<5;i++){
            std::cin>>scores[i];
        }
    }
    int calculateTotalScore(){
        int sum{0};
        for(int score: scores)
            sum+=score;
        return sum;
    }
};

