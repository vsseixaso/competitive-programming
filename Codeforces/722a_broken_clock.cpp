#include <cstdio>
int type, hour, minute;

int main() {
        scanf("%d", &type);
        scanf("%d:%d", &hour, &minute);
        if(type==12) {
                if(hour>12) {
                        hour%=10;
                }
                if(hour<1) {
                        hour=10;
                }
        } else {
                if(hour>23) {
                        hour%=10;
                }
        }
        if(minute>=60) {
                minute%=10;
        }
        if(hour<10) {
                printf("0");
        }
        printf("%d:",hour);
        if(minute<10) {
                printf("0");
        }
        printf("%d\n",minute);
        return 0;
}