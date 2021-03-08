#include <stdio.h>

unsigned int enterNumber();
void check(unsigned int a);

int main() {    
    while (1)
    {
        check(enterNumber()); 
    }
    return 0;
}
unsigned int enterNumber(){
    unsigned int num;
    printf("Enter your number: ");
    scanf("%d",&num);
    return num;
}
void check(unsigned int a){
    unsigned int num;
    unsigned int num2;
    unsigned int num3;
    num = a;
    num2 = a;
    unsigned int count = 0;
    unsigned int long_1 = 0;
    unsigned int result= 0;
    unsigned int x;
    for (int i = 0; i < 16; i++)
    {
        if ((num & 1) == 1)
        {
            count = count +1;
        }
        else
        {
            x =  1<<count;
            num2 = num2 | x;
            num3 = num2;
            while ((num3 & 1) == 1)
            {
                long_1 = long_1 +1;
                num3 = num3>>1;
            }
            num2 = num2 >> (count+1);
            if (result < long_1)
            {
                result = long_1;
            }
            count = 0;
            long_1 = 0;
        }
        num = num >> 1;
    }
    printf("Result  = %d \n",result);
}