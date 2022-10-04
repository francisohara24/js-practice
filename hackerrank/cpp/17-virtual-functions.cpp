//
// Created by franc on 8/21/2022.
//
#include <iostream>

int idProf = 0;
int idStud = 0;

class Person{
protected:
    std::string name;
    int age;
public:
    virtual void getdata(){}
    virtual void putdata(){}
};

class Professor: public Person{
    int publications, cur_id = ++idProf;
public:
    void getdata() override{
        std::cin>>this->name>>this->age>>this->publications;
    }
    void putdata() override{
        std::cout<<this->name<<" "<<this->age<<" "<<this->publications<<" "<<this->cur_id<<std::endl;
    }
};

class Student: public Person{
    int marks[6], cur_id = ++idStud;
public:
    void getdata() override{
        std::cin>>this->name>>this->age;
        for(int & mark: this->marks) std::cin>>mark;
    }
    void putdata() override{
        int sum=0;
        for(int mark: this->marks) sum+= mark;
        std::cout<<this->name<<" "<<this->age<<" "<<sum<<" "<<cur_id<<std::endl;
    }
};
