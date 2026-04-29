// #include <stdio.h>
// void print_multiplication_table(int num)
// {
//     for (int i = 1; i <= 10; i++)
//     {
//         printf("%d * %d = %d", num, i, num * i);
//         printf("\n");
//     }
// }
// int main()
// {
//     int num = 3;
//     print_multiplication_table(num);
// }

#include <stdio.h>

// void chqarish(int a, int b){
//     for(int i=a; i<=b; i++){
//         printf("%d ", i);
//     }
// }
// int main(){
//     int a=3, b=7;
//     chqarish(a, b);
// }

// void belgi_chiqarish(char c, int n){
//     for(int i=0; i<n; i++){
//         printf(" %c", c);
//     }
// }
// int main(){
//     char c='#';
//     int n=3;
//     belgi_chiqarish(c, n);
// }

// void chiqarish(int n)
// {
//     for (int i = 1; i <= n; i++)
//     {
//         if (i % 2 == 0)
//         {
//             printf("%d", i);
//         }
//     }
//     printf("\n");
//     for (int i = n; i >= 1; i--)
//     {
//         if (i % 2 != 0)
//         {
//             printf("%d", i);
//         }
//     }
// }
// int main()
// {
//     int n = 10;
//     chiqarish(n);
// }

// void tortburchak(int n, int m)
// {
//     for (int i = 0; i < n; i++)
//     {
//         for (int j = 0; j < m; j++)
//         {
//             printf("* ");
//         }
//         printf("\n");
//     }
// }
// int main()
// {
//     int n = 4, m = 4;
//     tortburchak(n, m);
// }

// void kabisa(int yil){
//     if(yil%400==0 || yil%4==0 && yil%100!=0){
//         printf("Kabisa yili");
//     }else{
//         printf("kabisa yili emas");
//     }
// }
// int main(){
//     int yil=2023;
//     kabisa(yil);
// }

// void harf_tekshirish(char c)
// {
//     if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'))
//     {
//         printf("Harf");
//     }
//     else
//     {
//         printf("Harf emas");
//     }
// }
// int main(){
//     char c='6';
//     harf_tekshirish(c);
// }

// void sonmi(char c)
// {
//     if (c >= '0' && c <= '9')
//     {
//         printf("Son");
//     }
//     else
//     {
//         printf("Son emas");
//     }
// }
// int main()
// {
//     char c = '5';
//     sonmi(c);
// }

// void kichikmi_kattami(char c)
// {
//     if (c >= 'A' && c <= 'Z')
//     {
//         printf("Katta harf");
//     }
//     else if (c >= 'a' && c <= 'z')
//     {
//         printf("Kichik harf");
//     }
//     else
//     {
//         printf("Harf emas");
//     }
// }
// int main()
// {
//     char c = 'A';
//     kichikmi_kattami(c);
// }

// void tubmi(int son)
// {
//     if (son <= 1)
//     {
//         printf("Tub son emas");
//         return;
//     }
//     int count = 0;
//     for (int i = 2; i < son; i++)
//     {
//         if (son % i == 0)
//         {
//             count++;
//             break;
//         }
//     }
//     if (count == 0)
//     {
//         printf("tub son");
//     }
//     else
//     {
//         printf("Tub son emas");
//     }
// }
// int main()
// {
//     int son = 17;
//     tubmi(son);
// }



// void tortburchak(int a, int b){
//     for(int i=1; i<=a; i++){
//         for(int j=1; j<=b; j++){
//             if(i==1 || i==a || j==1 || j==b){
//                 printf("*");
//             }else{
//                 printf(" ");
//             }
//         }
//         printf("\n");
//     }
// }
// int main(){
//     int a=4, b=5;
//     tortburchak(a, b);
// }




