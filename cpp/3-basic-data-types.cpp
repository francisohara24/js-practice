//
// Created by franc on 8/21/2022.
//
#include <cstdio>

int main() {
    int a;
    long b;
    char c;
    float d;
    double e;
    char buffer;
    scanf("%d", &a);
    scanf("%ld", &b);
    scanf("%c", &buffer);
    scanf("%c", &c);
    scanf("%f",&d);
    scanf("%lf", &e);
    printf("%d\n%ld\n%c\n%0.3f\n%0.9lf", a,b,c,d,e);
    return 0;
}
