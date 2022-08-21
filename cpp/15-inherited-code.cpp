//
// Created by franc on 8/21/2022.
//


/* Define the exception here */
class BadLengthException{
public:
    int number;
    BadLengthException(int n){
        number = n;
    }
    int what(){
        return number;
    }
};

