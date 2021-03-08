#include <stdio.h>
static int a = 0;
static void count(int i)
{
    static int num = 0;
    num += i;
    printf("current value of num: %d\n", num);
}
int main()
{
    a += 1;
    printf("value of a: %d\n", a);
    count(1);
    count(3);
    return 0;
}