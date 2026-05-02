#include <stdio.h>

int main()
{
    int a = 123;
    int yuzlik, onlik, birlik;
    yuzlik = a / 100;
    birlik = a % 10;
    onlik = a / 10 % 10;
    printf("%d%d%d", birlik, yuzlik, onlik);
}