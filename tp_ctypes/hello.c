#include<stdio.h>
#include<stdlib.h>
#include"hello.h"

void sayHello()
{
    printf("Hello from C\n");
}

void hello(const char *name)
{
    printf("Hello %s\n",name);
}