#include <stdio.h>

int main()
{
    int a = 3665;
    int soat = a / 3600;
    int daqiqa = a / 3600 % 60;
    int sekund = a % 10;
    printf("%d soat, %d daqiqa, %d sekund", soat, daqiqa, sekund);
}