#include <stdio.h>

int main()
{
    int son = 5;
    if (son > 7 || son <= 0)
    {
        printf("1-7 oraligida son kiriting.");
    }
    else if (son == 7)
    {
        printf("Dam olish kuni");
    }
    else
    {
        printf("Ish kuni");
    }
}