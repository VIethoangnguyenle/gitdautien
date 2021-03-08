#include<stdio.h>

int add(int a, int b){
    printf("a + b = %d\n",(a+b));
}
void enter_number(int a, int b, int* val_a,int* val_b){
    printf("Enter a: ");
    scanf("%d",&a);
    printf("Enter b: ");
    scanf("%d",&b);
    *val_a = a;
    *val_b = b; 
}
int main(){
    int (*func_pointer)(int,int);
    int a , b, val_a,val_b;
    func_pointer = &add;
    while (1)
    {
        enter_number(a,b,&val_a,&val_b);
        (*func_pointer)(val_a,val_b);
    }
    return 0;
}//sdsdsdsd