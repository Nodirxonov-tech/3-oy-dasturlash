#include <stdio.h>

int main()
{
    int a, b, c, d, e;
    printf("Yoshni kiriting: ");
    scanf("%d", &a);

    printf("Yoshni kiriting: ");
    scanf("%d", &b);

    printf("Yoshni kiriting: ");
    scanf("%d", &c);

    printf("Yoshni kiriting: ");
    scanf("%d", &d);

    printf("Yoshni kiriting: ");
    scanf("%d", &e);

    float orta = (a + b + c + d + e) / 5;
    printf("Ortacha yosh: %.1f", orta);
}