#include "stdio.h"
// 编译方法: gcc -fPIC -shared ./c死循环.c -o liba.so

void loop()
{
    printf("start...\n");
    while(1) {
    }
}
