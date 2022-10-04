//
// Created by franc on 8/21/2022.
//
#include <iostream>
/*
 * Create classes Rectangle and RectangleArea
 */
class Rectangle{
public:
    int width;
    int height;

    void display(){
        std::cout<<this->width<<" "<<this->height<<std::endl;
    }
};

class RectangleArea: public Rectangle{
public:
    void read_input(){
        std::cin>>this->width;
        std::cin>>this->height;
    }
    void display(){
        std::cout<<width * height;
    }
};
