#include <stdio.h>

int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    if (a==b && b==c) {
        printf("%d", 10000+a*1000);
    }
    else if (a==b || b==c) {
        printf("%d", 1000+b*100);
    }
    else if (c==a) {
        printf("%d", 1000+a*100);
    }
    else if (a>b) {
        if (c>a) {
            printf("%d", 100*c);
        }
        else {
            printf("%d", 100*a);
        }
    }
    else {
        if (c>b) {
            printf("%d", 100*c);
        }
        else {
            printf("%d", 100*b);
        }
    }

    return 0;
}